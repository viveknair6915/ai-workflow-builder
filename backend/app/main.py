from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .db import Base, engine, SessionLocal
from .models import Document, ChatLog
from .vector_store import get_collection
from .llm import get_embedding, ask_llm
from .serpapi import web_search
from .utils import extract_text_from_pdf
import os, shutil, tempfile

app = FastAPI(title="AI Workflow Builder API", version="1.0.0")
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Workflow Builder API", "status": "running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not file.filename.lower().endswith('.pdf'):
            raise HTTPException(status_code=400, detail="Only PDF files are supported")
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
        
        text = extract_text_from_pdf(tmp_path)
        os.remove(tmp_path)
        
        if not text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")
        
        # Split text into chunks (simple split for demo)
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        collection = get_collection("docs")
        embeddings = [get_embedding(chunk) for chunk in chunks]
        ids = [f"{file.filename}_{i}" for i in range(len(chunks))]
        collection.add(documents=chunks, embeddings=embeddings, ids=ids)
        
        # Save doc metadata
        db = SessionLocal()
        doc = Document(filename=file.filename, metadata="{}")
        db.add(doc)
        db.commit()
        db.close()
        
        return {"message": "Uploaded and processed", "chunks": len(chunks), "filename": file.filename}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@app.post("/run_workflow")
async def run_workflow(
    user_query: str = Form(...),
    use_kb: bool = Form(True),
    use_web: bool = Form(False),
    custom_prompt: str = Form("")
):
    try:
        if not user_query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        context = ""
        if use_kb:
            collection = get_collection("docs")
            query_emb = get_embedding(user_query)
            results = collection.query(query_embeddings=[query_emb], n_results=3)
            context = " ".join(results["documents"][0]) if results["documents"] else ""
        
        if use_web:
            web_result = web_search(user_query)
            context += f"\nWeb: {web_result}"
        
        prompt = custom_prompt if custom_prompt else user_query
        response = ask_llm(prompt, context=context)
        
        # Save chat log
        db = SessionLocal()
        log = ChatLog(workflow=f"KB:{use_kb},WEB:{use_web}", user_query=user_query, response=response)
        db.add(log)
        db.commit()
        db.close()
        
        return {"response": response, "context_used": bool(context)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing workflow: {str(e)}")

@app.get("/chat_logs")
def get_logs():
    try:
        db = SessionLocal()
        logs = db.query(ChatLog).all()
        db.close()
        return [{"query": l.user_query, "response": l.response, "time": l.timestamp} for l in logs]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving logs: {str(e)}") 
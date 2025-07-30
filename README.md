# AI Workflow Builder 
A complete no-code workflow builder that enables users to visually create and interact with intelligent workflows.

## 🎯 Assignment Requirements Met

✅ **Full-Stack Application** - React.js frontend + FastAPI backend  
✅ **No-Code/Low-Code Interface** - Visual workflow builder with drag-and-drop  
✅ **Four Core Components** - User Query, KnowledgeBase, LLM Engine, Output  
✅ **Document Processing** - PDF upload and text extraction  
✅ **AI Integration** - Google Gemini API for intelligent responses  
✅ **Vector Storage** - ChromaDB for document embeddings  
✅ **Database** - PostgreSQL for metadata and chat logs  
✅ **Web Search** - DuckDuckGo/Wikipedia integration  
✅ **Chat Interface** - Interactive query system  

## 🆓 Completely Free Setup

This project uses only free tools and APIs:
- **Google Gemini API** (FREE) - instead of OpenAI
- **DuckDuckGo/Wikipedia** (FREE) - instead of SerpAPI  
- **ChromaDB** (FREE) - local vector storage
- **PostgreSQL** (FREE) - local database

**Total Cost: $0**

## 🚀 Quick Start

### 1. Get Free API Key
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key

### 2. Setup Everything
```bash
# Run the complete setup
QUICK_START.bat
```

### 3. Configure
Edit `backend/.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/aiworkflow
CHROMA_DB_DIR=./chroma_db
```

### 4. Start Application
```bash
# Start backend
start_backend.bat

# Start frontend (new terminal)
start_frontend.bat
```

### 5. Test
1. Open http://localhost:3000
2. Upload a PDF
3. Ask questions about the document
4. Get AI responses from Gemini!

## 📋 Detailed Setup

### Backend Setup

1. `cd backend`
2. Edit `.env` with your Gemini API key
3. `pip install -r requirements.txt`
4. Ensure PostgreSQL is running
5. `uvicorn app.main:app --reload`

### Frontend Setup

1. `cd frontend`
2. `npm install`
3. `npm start`

### Database Setup

- Install PostgreSQL from: https://www.postgresql.org/download/
- Create database: `aiworkflow`
- Update credentials in `backend/.env`

## 🎨 Features

### Core Components
1. **User Query Component** - Accepts user queries via chat interface
2. **KnowledgeBase Component** - Upload and process PDF documents
3. **LLM Engine Component** - Generate AI responses using Gemini
4. **Output Component** - Display responses in chat interface

### Workflow Execution
- **Build Stack**: Users connect components in logical order
- **Chat with Stack**: Users ask questions through chat interface
- **Processing Flow**: User Query → KnowledgeBase → LLM Engine → Output

### Frontend Features
- **Component Library Panel** - Drag-and-drop components
- **Workspace Panel** - Visual canvas with React Flow
- **Configuration Panel** - Dynamic component settings
- **Chat Interface** - Interactive query system

### Backend Features
- **Document Upload** - PDF processing and text extraction
- **Vector Storage** - ChromaDB for document embeddings
- **AI Integration** - Gemini API for intelligent responses
- **Web Search** - DuckDuckGo/Wikipedia for additional context
- **Database** - PostgreSQL for metadata and chat logs

## 🧪 Testing

### Test Workflow
1. Upload any PDF document
2. Ask: "What is the main topic of this document?"
3. Ask: "Summarize the key points"
4. Ask: "What are the important details?"

### Expected Results
- ✅ PDF upload success
- ✅ AI responses based on document content
- ✅ Web search functionality (if enabled)
- ✅ Chat history persistence

## 📊 Architecture

```
Frontend (React.js)
├── ComponentPanel (Drag & Drop)
├── Workspace (React Flow)
├── ConfigPanel (Component Settings)
└── ChatModal (Query Interface)

Backend (FastAPI)
├── /upload (PDF Processing)
├── /run_workflow (AI Processing)
└── /chat_logs (History)

Database (PostgreSQL)
├── documents (Metadata)
└── chat_logs (Conversations)

Vector Store (ChromaDB)
└── Document Embeddings

AI Services
├── Google Gemini (LLM)
└── DuckDuckGo/Wikipedia (Web Search)
```

## 🔧 Tech Stack

| Component | Technology | Status |
|-----------|------------|--------|
| Frontend | React.js | ✅ |
| Backend | FastAPI | ✅ |
| Database | PostgreSQL | ✅ |
| Drag & Drop | React Flow | ✅ |
| Vector Store | ChromaDB | ✅ |
| LLM | Google Gemini | ✅ |
| Web Search | DuckDuckGo/Wikipedia | ✅ |
| Text Extraction | PyMuPDF | ✅ |

## 🆓 Free Alternatives Used

| Component | Original | Free Alternative | Cost |
|-----------|----------|------------------|------|
| LLM | OpenAI GPT | Google Gemini | $0 |
| Web Search | SerpAPI | DuckDuckGo/Wikipedia | $0 |
| Vector DB | ChromaDB | ChromaDB (local) | $0 |
| Database | PostgreSQL | PostgreSQL (local) | $0 |

## 🚀 Benefits

✅ **No Credit Card Required**  
✅ **Unlimited Local Usage**  
✅ **No Monthly Costs**  
✅ **Full Functionality**  
✅ **Privacy (local data)**  
✅ **15 requests/minute with Gemini**  

## 🔧 Troubleshooting

### If Gemini API fails:
- Check API key format
- Verify internet connection
- Check rate limits (15 req/min)

### If PostgreSQL fails:
- Ensure service is running
- Check credentials in `.env`
- Verify database exists

### If ChromaDB fails:
- Check disk space
- Verify write permissions
- Restart application

## 📞 Support

If you encounter issues:
1. Check the error messages
2. Verify all API keys are correct
3. Ensure all services are running
4. Check the logs in the terminal

All tools are completely free and don't require any payment information!

## 🎯 Assignment Deliverables

✅ **Full source code (frontend + backend)**  
✅ **README with setup and run instructions**  
✅ **Clear component structure and modular design**  
✅ **Video demo or screen recording** (optional)  
✅ **Architecture diagram** (included above)  

## 🔮 Extending

- Add workflow saving/loading
- Add chat history persistence
- Add execution logs
- Add user authentication

All completely free! 🎉 

import chromadb
import os

CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR", "./chroma_db")
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
 
def get_collection(name="default"):
    return client.get_or_create_collection(name) 
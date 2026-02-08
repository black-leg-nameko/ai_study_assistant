from fastapi import FastAPI
from pydantic import BaseModel
from .rag import add_document, ask

app = FastAPI()

class Doc(BaseModel):
    text: str

class Question(BaseModel):
    query: str

@app.post("/add")
def add(doc: Doc):
    add_document(doc.text)
    return {"status": "ok"}

@app.post("/ask")
def ask_question(q: Question):
    answer = ask(q.query)
    return {"answer": answer}

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    reader = PdfReader(file.file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    add_document(text)
    return {"status": "pdf added", "length": len(text)}

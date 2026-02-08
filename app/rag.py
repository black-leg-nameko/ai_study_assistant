import chromadb
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma = chromadb.Client()
collection = chroma.get_or_create_collection("docs")

def add_document(text: str):
    collection.add(
            documents=[text],
            ids=[f"doc-{collection.count()}"]
    )

def ask(query: str):
    results = collection.query(
            query_texts=[query],
            n_results=3
    )

    context = "\n".join(results["documents"][0])

    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは大学生向けの学習アシスタントです。"},
                {"role": "user", "content": F"以下の資料に基づいて答えてください:\n{context}\n\n質問: {query}"}
            ]
        )

    return response.choices[0].message["content"]

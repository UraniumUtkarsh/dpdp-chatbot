import os
import time

import chromadb

from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer


# Load environment variables
load_dotenv()


# Gemini client
client_genai = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# Embedding model
embedding_model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)


# ChromaDB setup
client = chromadb.PersistentClient(
    path="./vectorstore"
)

collection = client.get_collection(
    name="dpdp_docs"
)


def query_documents(query, top_k=2):

    query_embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


def generate_response(query):

    results = query_documents(query)

    documents = results.get("documents", [[]])

    metadatas = results.get("metadatas", [[]])

    chunks = documents[0]

    # No retrieval found
    if not chunks:

        return {
            "answer": (
                "I could not find relevant "
                "information in the provided "
                "DPDP documents."
            ),
            "sources": []
        }

    # Build context
    context = "\n\n".join(chunks)

    print("\nRetrieved Chunks:\n")
    print(context)

    # Prompt
    prompt = f"""
You are a helpful assistant for India's
DPDP Act and related rules.

IMPORTANT RULES:
- Answer ONLY from provided context
- Do NOT hallucinate
- Do NOT generate fake legal advice
- If relevant information exists in context,
  summarize it clearly.
- Only say "I could not find..."
  when context is completely unrelated.
- Explain legal concepts in simple language
- Support both Hindi and English
- Stay restricted to DPDP/privacy topics only

Context:
{context}

Question:
{query}
"""

    answer = ""

    # Retry logic
    for attempt in range(3):

        try:

            response = client_genai.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )

            answer = response.text

            break

        except Exception as e:

            answer = f"Model Error: {str(e)}"

            print(f"\nAttempt {attempt + 1} failed:")
            print(e)

            time.sleep(2)

    # Remove duplicate sources
    unique_sources = []

    seen = set()

    for source in metadatas[0]:

        source_name = source.get("source")

        if source_name not in seen:

            seen.add(source_name)

            unique_sources.append(source)

    return {
        "answer": answer,
        "sources": unique_sources
    }
import os

import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


# Multilingual embedding model
model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)

# ChromaDB setup
client = chromadb.PersistentClient(
    path="./vectorstore"
)

collection = client.get_or_create_collection(
    name="dpdp_docs"
)

DOCUMENTS_PATH = "./documents"


def extract_text_from_pdf(pdf_path):

    try:

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return text

    except Exception as e:

        print(f"Error reading PDF {pdf_path}: {e}")

        return ""


def chunk_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def ingest_documents():

    doc_id = 0

    total_chunks = 0

    print("\nScanning documents folder...\n")

    # Walk through ALL folders and subfolders
    for root, dirs, files in os.walk(DOCUMENTS_PATH):

        for file in files:

            if file.endswith(".pdf"):

                pdf_path = os.path.join(
                    root,
                    file
                )

                print(f"\nIngesting: {pdf_path}")

                # Extract text
                text = extract_text_from_pdf(
                    pdf_path
                )

                # Check extraction
                print(
                    f"Extracted text length: {len(text)}"
                )

                if len(text.strip()) == 0:

                    print(
                        f"Skipping empty/scanned PDF: {file}"
                    )

                    continue

                # Chunking
                chunks = chunk_text(text)

                print(
                    f"Created {len(chunks)} chunks"
                )

                # Store chunks
                for chunk in chunks:

                    try:

                        embedding = model.encode(
                            chunk
                        ).tolist()

                        collection.add(
                            documents=[chunk],
                            embeddings=[embedding],
                            ids=[str(doc_id)],
                            metadatas=[{
                                "source": file,
                                "path": pdf_path
                            }]
                        )

                        doc_id += 1
                        total_chunks += 1

                    except Exception as e:

                        print(
                            f"Error storing chunk: {e}"
                        )

    print(
        f"\nTotal chunks stored: {total_chunks}"
    )

    print("\nIngestion completed successfully.")


if __name__ == "__main__":

    ingest_documents()
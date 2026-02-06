from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")

doc = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result = embedding.embed_documents(doc)
print(str(result))
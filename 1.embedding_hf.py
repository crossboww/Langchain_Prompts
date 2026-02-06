from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")

doc = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

doc_emb = embedding.embed_documents(doc)
query_emb = embedding.embed_query(query)

score = cosine_similarity([query_emb], doc_emb)[0]
# print(score)

# print(list(enumerate(score)))
index, score = sorted(list(enumerate(score)), key=lambda x:x[1])[-1]

print(query)
print(doc[index])
print("similarity score is:", score)
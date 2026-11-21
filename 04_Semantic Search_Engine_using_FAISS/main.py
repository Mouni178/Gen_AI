from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 1. Load the embedding model
print("Loading embedding model...")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 2. Create a collection of documents
documents = [
    "Python is a popular programming language.",
    "Artificial intelligence enables machines to learn.",
    "Java is widely used for software development.",
    "Deep learning is a branch of machine learning.",
    "Data science involves analyzing and interpreting data.",
    "Natural language processing helps computers understand human language."
]

# 3. Generate embeddings for documents
print("Generating document embeddings...")

embeddings = model.encode(
    documents,
    normalize_embeddings=True
)

# Convert embeddings into NumPy float32 array
embeddings = np.array(embeddings, dtype="float32")

# 4. Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

# 5. Add document embeddings to FAISS
index.add(embeddings)

print("\nSemantic Search Engine is ready!")

# 6. Search function
def semantic_search(query, top_k=3):

    # Generate embedding for user query
    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    # Search in FAISS
    scores, indices = index.search(query_embedding, top_k)

    # Display results
    print("\nSearch Query:", query)
    print("\nTop Matching Results:")

    for rank, (score, idx) in enumerate(
        zip(scores[0], indices[0]), start=1
    ):
        if idx == -1:
            continue

        print(f"\n{rank}. {documents[idx]}")
        print(f"Similarity Score: {score:.4f}")


# 7. Get user input
while True:

    query = input("\nEnter your search query (or type 'exit'): ")

    if query.lower() == "exit":
        print("Search engine closed.")
        break

    if not query.strip():
        print("Please enter a valid query.")
        continue

    semantic_search(query)
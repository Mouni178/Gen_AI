from sentence_transformers import SentenceTransformer
# Load pretrained embedding model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded successfully!")

# Input sentence
sentence = "I love programming in Python."

# Generate embedding
embedding = model.encode(sentence)

print("\nOriginal Sentence:")
print(sentence)

print("\nGenerated Embedding:")
print(embedding)

print("\nEmbedding Dimensions:")
print(len(embedding))

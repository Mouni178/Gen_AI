import ollama
MODEL = "gemma3:1b"
def generate_response(question):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response["message"]["content"]
def main():
    print("LOCAL AI CHATBOT")
    while True:
        question = input("\nYou: ")
        if question.lower() == "exit":
            print("Goodbye!")
            break
        try:
            answer = generate_response(question)
            print("\nAI:", answer)
        except Exception as e:
            print("Error:", e)
if __name__ == "__main__":
    main()
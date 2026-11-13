import os
from dotenv import load_dotenv
from openai import OpenAI, APIStatusError
# STEP 1: Load environment variables
load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")
if not api_key:
    raise ValueError("NVIDIA API Key not found!")
print("API Key loaded successfully!")
# STEP 2: Initialize NVIDIA client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)
print("NVIDIA client initialized!")
# STEP 3: Check available models
print("\nChecking available models...\n")
try:
    models = client.models.list()
    available_models = models.data
    print("Available models:")
    for model in available_models:
        print(model.id)
except APIStatusError as e:
    print("Model listing failed!")
    print("Status:", e.status_code)
    print("Details:", e.response.text)
    raise SystemExit(1)
# STEP 4: Select a model
MODEL_ID = "openai/gpt-oss-20b"
print("\nSelected Model:", MODEL_ID)
# STEP 5: Send prompt to LLM
print("\nSending request to NVIDIA LLM...\n")
try:
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": "Explain Generative AI in simple words with examples."
            }
        ],
        temperature=0.7,
        max_tokens=500
    )
    # STEP 6: Extract AI response
    answer = response.choices[0].message.content
    print("=" * 50)
    print("AI GENERATED RESPONSE")
    print("=" * 50)
    print(answer)
    print("=" * 50)
except APIStatusError as e:
    print("\nAPI REQUEST FAILED!")
    print("Status Code:", e.status_code)
    print("Error Details:", e.response.text)
    if e.status_code == 410:
        print("\nPossible issue:")
        print("NVIDIA hosted inference access may not")
        print("be enabled for your account.")
        print("Contact NVIDIA Developer Support.")
    elif e.status_code == 401:
        print("Check whether your API key is valid.")
    elif e.status_code == 404:
        print("Check the model ID and endpoint.")
except Exception as e:
    print("\nUnexpected Error:", str(e))

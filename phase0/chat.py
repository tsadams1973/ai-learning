from ollama import chat

response = chat(
    model="qwen3.8",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello and tell me one thing about local AI."}
    ]
)   

print(response["message"]["content"])
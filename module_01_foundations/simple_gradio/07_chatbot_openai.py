import os
from pathlib import Path
 
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
 
# Load API key from project root .env
load_dotenv(Path(__file__).resolve().parents[2] / ".env", override=True)
 
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "").strip().strip('"').strip("'")
)
 
def chat(message: str, history: list):
    try:
        stream = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role":"system", "content":"You are a helpful assistant. Be concise."},
                {"role":"user", "content":message}
            ],
            stream=True,
            max_tokens=500
        )
 
        partial = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                partial += delta
                yield partial
   
    except Exception as e:
        yield f"Error: {e}"
 
demo = gr.ChatInterface(
    fn=chat,
    title="OpenAI ChatBot",
    description=(
        "Chect with GPT-4o-mini - responses stream in real-time"
        "No memory - each message is independent!"
    ),
    examples=[
        "What is Python in one sentence?",
        "Write a haiku about programming",
        "Expain APIs like i'm 10 years old."
    ]
)
 
if __name__ == "__main__":
    demo.launch()
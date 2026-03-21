import os
from pathlib import Path
 
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
 
# Load API key from project root .env
load_dotenv(Path(__file__).resolve().parents[2] / ".env", override=True)
 
API_KEY=os.getenv("OPENAI_API_KEY", "").strip().strip('"').strip("'")
 
client = OpenAI(
    api_key=API_KEY
)
 
SYSTEMP_PROMPT = """You are a friendly and helpful assistant.
You remember everything the user has said in this conversation.
Be concise but warm. Use emoji occasionally."""
 
def chat_with_memory(message: str, history: list):
    messages = [
        {"role":"system", "content": SYSTEMP_PROMPT},
        *history,
        {"role":"user", "content":message},
    ]
 
    try:
        stream = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=messages,
            stream=True,
            max_tokens=500,
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
    fn=chat_with_memory,
    title="Chat with OpenAI and memory",
    description="This chatbot remembers everything...",
    examples=[
        "My name is Alice. I am 30 years old.",
        "What are 3 fun facts about Python and AI?",
        "Let's play a word game. I will say a word and you will reply with a similar one."
    ]
)
 
if __name__ == "__main__":
    demo.launch()
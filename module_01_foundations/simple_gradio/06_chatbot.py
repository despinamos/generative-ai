import gradio as gr
import time

def echo_bot(message: str, history:list):
    return f"You said: **{message}**\n\n I'm an echo bot - I repeat what you say"

def streaming_bot(message: str, history: list):
    response = f"You asked: {message}. Here are my thoughts about it"

    portal = ""
    for word in response.split():
        partial += word + " "
        time.sleep(0.2)
        yield partial.strip()

def personality_bot(message: str, history: list):
    user_turns = sum(1 for msg in history if msg.get("role") == "user")
    turn = user_turns + 1

    if turn == 1:
        response = f"Hello. This is our **first** exchange. You said: {message}"
    elif turn <= 3:
        response = f"Nice, turn **{turn}**. I remember that we've been chatting."
    else:
        response = f"Wow, turn **{turn}** already! We know each other. You said: {message}"
   
    response += f"\n History has **{len(history)}** messages so far"
    return response

demo = gr.ChatInterface(
    fn=streaming_bot,
    title="My first chatbot",
    description="A simple chatbot"
)

if __name__ == "__main__":
    demo.launch()
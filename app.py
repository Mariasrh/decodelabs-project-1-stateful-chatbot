import os

import gradio as gr

import google.generativeai as genai

from dotenv import load_dotenv



# Load API key from the .env file

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



# Pick the first available model to avoid errors

def get_best_model():

    for m in genai.list_models():

        if 'generateContent' in m.supported_generation_methods:

            return m.name

    return None



model = genai.GenerativeModel(get_best_model())



# This object keeps track of our conversation history (Stateful)

chat_session = model.start_chat(history=[])



# Main function to handle the chat

def predict(message, history):

    # Check if the user sent something

    if not message or message.strip() == "":

        return "Please type something."

   

    # Send message to Gemini and get the reply

    try:

        response = chat_session.send_message(message)

        return response.text

    except Exception as e:

        # Simple fix if the free plan limit is reached

        return "Rate limit hit, please wait a minute."



# Create and run the interface

demo = gr.ChatInterface(fn=predict, title="My Stateful Chatbot")



if __name__ == "__main__":

    demo.launch()



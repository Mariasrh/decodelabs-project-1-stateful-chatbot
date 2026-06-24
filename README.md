# DecodeLabs - Project 1: Stateful AI Chatbot

Welcome to my first project as an AI Engineer intern at DecodeLabs. This project focuses on transforming a "stateless" LLM into a contextual conversational agent capable of maintaining memory throughout a live session.

##  Project Goal
The objective is to build an intelligent chatbot that "remembers" the history of previous messages in an active session, utilizing **Stateful Architecture** rather than processing messages in isolation.

##  Key Features
- **API Integration:** Secure connection to a frontier LLM using the official Google Gemini SDK.
- **State Management (Stateful):** Implements an in-memory `chat_session` array to store and track conversation history.
- **Contextual Mechanics:** Every interaction dynamically appends to the history payload, allowing the model to understand the conversational flow.
- **Structural Validation:** Includes an explicit "gatekeeper" to filter out empty or whitespace-only inputs, preventing API 400 errors.

## Technical Architecture


The project follows a memory loop sequence for every turn:
1. **Ingest & Append:** User input is validated and added to the local history list as a structured object.
2. **Transmit & Record:** The full updated history list is passed to the GenAI client, and the model's response is appended to the same list.

##  Project Structure
- `app.py`: The main chatbot engine (business logic and Gradio interface).
- `.env`: Secure configuration file for the API Key (excluded from Git).
- `requirements.txt`: Project dependencies (`gradio`, `google-generativeai`, `python-dotenv`).
- `.gitignore`: Prevents sensitive files like `.env` from being uploaded.

##  Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/Mariasrh/decodelabs-project-1-stateful-chatbot.git](https://github.com/Mariasrh/decodelabs-project-1-stateful-chatbot.git)

# My-Streamlit-AI

A small Streamlit chat app that talks to a local LLM through Ollama. Type a prompt, hit enter, and the app sends it to the `mistral` model running on your machine and displays the response. It was an early experiment in wiring a chat UI to a locally hosted model.

## What it does

`main.py` is deliberately simple:

- A text input for your prompt and a submit button
- Calls `ollama.chat` with the `mistral` model and your message
- Displays the model's reply on the page

No chat history, no streaming, no extra features. Just the shortest path from a Streamlit input box to a local LLM and back.

## How to run

You need [Ollama](https://ollama.com) installed with the mistral model pulled:

```bash
ollama pull mistral
```

Then:

```bash
git clone https://github.com/suhasaitham22/My-Streamlit-AI.git
cd My-Streamlit-AI
pip install -r requirements.txt
streamlit run main.py
```

The app expects Ollama to be running locally (the default `http://localhost:11434`).

## Tech stack

Streamlit, Ollama Python client, Mistral (local LLM).

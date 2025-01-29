import streamlit as st
import ollama

# Streamlit UI
st.title("💬 Chat with LLM (Ollama)")

# Text input for user message
user_input = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            # Call Ollama API
            response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_input}])
            st.write("### Response:")
            st.write(response["message"]["content"])
    else:
        st.warning("Please enter a prompt!")

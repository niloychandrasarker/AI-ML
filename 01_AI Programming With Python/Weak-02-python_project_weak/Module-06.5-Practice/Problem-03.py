# Problem 3
# Build an app that:
# Takes a sentence from user
# Sends to Gemini with instruction:
#  “Improve this sentence professionally”
# Displays improved version
# Example:
#  Input: "i want job"
#  Output: "I am seeking a professional opportunity."



import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

sentence = st.text_input("Enter your sentence")
improve_sentence = st.button("Improve Sentence")   

if improve_sentence:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Improve this sentence professionally: {sentence}"
    )
    st.markdown(response.text)

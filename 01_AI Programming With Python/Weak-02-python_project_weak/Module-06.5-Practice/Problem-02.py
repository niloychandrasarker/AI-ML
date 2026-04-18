# Problem 2
# Create an app that:
# Takes a prompt from user
# Sends it to Gemini API
# Displays the generated response

import streamlit as st
from google import genai
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = st.text_input("Enter your prompt")
Generate_response = st.button("Generate Response")

if Generate_response:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    st.markdown(response.text)

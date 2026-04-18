from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def issue(images):
    prompt="""Identify the issues in the picture """
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [images, prompt]
    )
    return response.text

def code_solution_genarator(images, option):
    prompt=f"""Genarate the {option} based on the picture.
        Make sure the solution is relevant to the content of the picture and are appropriate for the selected option."""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [images, prompt]
    )
    return response.text
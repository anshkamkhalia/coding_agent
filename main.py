import os # environment/file handling
from dotenv import load_dotenv # for env variables
from google import genai # llm
import sys # debugging
from google.genai import types

# import tools
from functions.get_files_info import get_files_info
from functions.read_file_contents import read_file_contents
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():

    load_dotenv() # loads .env file
    api_key = os.environ.get("GEMINI_API_KEY") # loads our api key securely

    client = genai.Client(api_key=api_key) # initialize client with api key

    # check if user entered a prompt
    if len(sys.argv) < 2:
        print("enter a prompt")

    prompt = sys.argv[1] # extract prompt

    # store in Content objects
    messages = [
        types.Content(role='user', parts=[types.Part(text=prompt)])
    ]

    # get response
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages
    )

    print(response.text)

print(run_python_file('./', 'input_test.py'))
import os # environment/file handling
from dotenv import load_dotenv # for env variables
from google import genai # llm
import sys # debugging
from google.genai import types
from agent_config import WORKING_DIRECTORY, PROJECT_NAME, MAX_ITERS

# import tools
from functions.get_files_info import get_files_info
from functions.read_file_contents import read_file_contents
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.call_function import execute_function_call

# import schemas
from functions.get_files_info import get_files_info_schema
from functions.read_file_contents import read_file_contents_schema
from functions.write_file import write_file_schema
from functions.run_python_file import run_python_file_schema

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

    # list available functions for the model to use
    available_functions = types.Tool(
        function_declarations=[
            get_files_info_schema,
            write_file_schema,
            read_file_contents_schema,
            run_python_file_schema,
        ]
    )

    # to call/match functions
    FUNCTION_MAP = {
        "get_files_info": get_files_info,
        "write_file": write_file,
        "read_file_contents": read_file_contents,
        "run_python_file": run_python_file,
    }


    # create a system prompt
    SYSTEM_PROMPT = (
    f"You are a helpful AI coding agent designed to help the user with building a(n) {PROJECT_NAME}. "
    f"You are required to stay within the hardcoded WORKING_DIRECTORY={WORKING_DIRECTORY} for security reasons. "
    f"Here are your available functions:\n"
    f"1. get_files_info(working_directory, directory) -> lists directory contents\n"
    f"2. write_file(working_directory, filepath, content) -> writes to a file\n"
    f"3. read_file_contents(working_directory, filepath) -> reads a file\n"
    f"4. run_python_file(working_directory, filepath) -> executes a python file\n"
)


    # create config
    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, # pass sys prompt
                                         tools=[available_functions]) # pass tools

    for _ in range(0, MAX_ITERS):

        # get response
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=config
        )

        if response is None:
            print('error with response')
            return

        # update message history
        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue

                # candidate.content.parts is the list of Parts
                parts = candidate.content.parts  

                messages.append(
                    types.Content(
                        role="assistant",
                        parts=parts
                    )
                )

        # call appropriate function
        if response.function_calls:
            for call in response.function_calls:
                result = execute_function_call(call)
                print(result)
                messages.append(
                    types.Content(
                        role="user",
                        parts=[types.Part(text=str(result))]
                    )
                )
            
        else:
            print(response.text)
            return

if __name__ == "__main__":
    main()
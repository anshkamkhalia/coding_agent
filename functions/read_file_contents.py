import os
from google.genai import types

MAX_CHARS = 10000 # to prevent overusing token limits

def read_file_contents(working_directory: str, filepath: str) -> str:

    # gets absolute paths
    abs_working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(abs_working_dir, filepath))

    # checks if file is in cwd
    if not abs_filepath.startswith(abs_working_dir):
        return f"error: {filepath} is not a valid file to access in the working directory"
    
    # checks if given path is actually a file
    if not os.path.isfile(os.path.join(abs_filepath)):
        return f'error: {filepath} is not a file'
    
    # read file contents
    try:
        with open(abs_filepath, "r") as f: # open in "r" to avoid corruption
            contents = f.read(MAX_CHARS) # truncate

    except Exception as e:
        return f"exception {Exception} occured when attempting to read the contents of {abs_filepath}"

    return contents

# schema
read_file_contents_schema = types.FunctionDeclaration(
    name='read_file_contents',
    description='Reads the contents of a specified file.',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory. The function restricts access to files within this directory."
            ),
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The relative filepath to the file desired to display the contents of.",
                nullable=False
            )
        },
        required=["working_directory", "filepath"]
    )
)

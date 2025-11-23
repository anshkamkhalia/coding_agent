import os
from google.genai import types

MAX_CHARS = 20000 # to prevent overusing token limits

def write_file(working_directory: str, filepath: str, content: str) -> str:

    # gets absolute paths
    abs_working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(abs_working_dir, filepath))

    # checks if file is in cwd
    if not abs_filepath.startswith(abs_working_dir):
        return f"error: {filepath} is not a valid file to write to in the working directory"
    
    # checks if given path is actually a file/actually exists
    if not os.path.isfile(os.path.join(abs_filepath)):
        return f'error: {filepath} is either not a file, or doesn\'t exist yet'
        
    # write to file
    try:
        with open(abs_filepath, "w") as f:
            f.write(content)
            return f''
    except Exception as e:
        return f'exception {Exception} occured when attempting to write to file'
    
# schema
write_file_schema = types.FunctionDeclaration(
    name='write_file',
    description='Overwrites the previous contents of a specified file with new content',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory. The function restricts access to files within this directory."
            ),
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="Relative filepath to the file that should have its contents overwritten.",
                nullable=False
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written into the given file."
            )
        },
        required=["working_directory", "filepath", "content"]
    )
)

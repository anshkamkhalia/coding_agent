import os
from google.genai import types

def create_file(working_directory:str, filepath: str, content: str=""):
    # gets absolute paths
    abs_path = os.path.abspath(os.path.join(working_directory, filepath))

    # checks if file is actually inside the workingt directory
    if not abs_path.startswith(os.path.abspath(working_directory)):
        return {"error" : "path out side working directory is not allowed"}
    
    # create parent directories if required
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)

    # create file
    try:
        with open(abs_path, "w") as f:
            f.write(content)
        return {"success": True, "path": filepath}
    except Exception as e:
        return {"error": str(e)}
    
# create schema
create_file_schema = types.FunctionDeclaration(
    name='create_file',
    description='Creates a python file in a specified location. Also creates parent directories if needed. Content may be passed to be written into the file instead of calling another function. File must stay inside the working directory.',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'working_directory': types.Schema(
                type=types.Type.STRING,
                description="Base working directory, should not deviate from the provided working directory.",
                nullable=False

            ),
            'filepath': types.Schema(
                type=types.Type.STRING,
                description="Relative filepath to the file that is wished to be created. May contain non-existent parent directories, will be created at runtime.",
                nullable=False
            ),
            'content': types.Schema(
                type=types.Type.STRING,
                description="Content that will be added into the file after creation. Is optional."
            )

        },
        required=['working_directory', 'filepath'],
    )
)
import os
import subprocess
import sys
from google.genai import types

def run_python_file(working_directory: str, filepath: str) -> dict:

    # gets absolute paths
    abs_working_dir = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(abs_working_dir, filepath))

    # checks if file is in cwd
    if not abs_filepath.startswith(abs_working_dir):
        return {'error': f"error: {filepath} is not a valid python file to run to in the working directory"}
    
    # checks if given path is actually a file/actually exists
    if not os.path.isfile(os.path.join(abs_filepath)):
        return {'error': f'error: {filepath} is either not a file, or doesn\'t exist yet'}
    
    # checks if a file is actually a python file
    if not abs_filepath.endswith(".py"):
        return {'error': f'error: {filepath} is not a python script'}

    # args for executing
    args = [
        sys.executable,
        abs_filepath,
        os.path.basename(abs_filepath)
    ]

    try:
        output = subprocess.run(args, capture_output=True) # runs the script

        return {
            'STDOUT': output.stdout.decode('utf-8'), # output
            'STDERR': output.stderr.decode('utf-8') # error
        }
    except Exception as e:
        return {'error': f'error while executing {filepath}: {e}'}

# schema
run_python_file_schema = types.FunctionDeclaration(
    name='run_python_file',
    description='Executes the specified python script',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory. The function restricts access to files within this directory."
            ),
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the file that should be executed.",
                nullable=False
            )
        },
        required=["working_directory", "filepath"]
    )
)

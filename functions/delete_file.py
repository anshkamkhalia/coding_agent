import os
from google.genai import types

def delete_file(working_directory: str, filepath: str):
    # get abolsute path
    abs_path = os.path.abspath(os.path.join(working_directory, filepath))

    # check if it is a python file
    if not abs_path.endswith(".py"):
        return {"error": "can only delete python files, tell me if require to delete a directory or other type of file"}
    
    try:
        os.remove(abs_path) # remove file
        return {'success': True, 'msg': f'successfully deleted {abs_path}'}
    except Exception as e:
        return {'error': f'exception {e} occured when attempting to remove {abs_path}'}
    
# schema
delete_file_schema = types.FunctionDeclaration(
    name='delete_file',
    description='Deletes a specified python file. USE EXTREMELY CAREFULLY',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'working_directory': types.Schema(
                type=types.Type.STRING,
                description='The base working directory. Should never deviate from the given hardcoded directory.',
                nullable=False,
            ),
            'filepath': types.Schema(
                type=types.Type.STRING,
                description='Relative filepath to the file that should be deleted.',
                nullable=False
            ),

        },
        required=['working_directory', 'filepath']
    )
)
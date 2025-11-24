from functions.get_files_info import get_files_info
from functions.read_file_contents import read_file_contents
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.create_file import create_file
from functions.delete_file import delete_file
from functions.install_dependencies import install_dependencies
from agent_config import WORKING_DIRECTORY

# to call/match functions
FUNCTION_MAP = {
        "get_files_info": get_files_info,
        "write_file": write_file,
        "read_file_contents": read_file_contents,
        "run_python_file": run_python_file,
        "create_file": create_file,
        "delete_file": delete_file,
        "install_dependencies": install_dependencies,
}

def execute_function_call(call):
    function_name = call.name
    function_args = {**call.args} # Create a mutable copy

    # Add working_directory to all function calls
    function_args['working_directory'] = WORKING_DIRECTORY

    if function_name in FUNCTION_MAP:
        function_to_call = FUNCTION_MAP[function_name]
        return function_to_call(**function_args)
    else:
        return f"Function {function_name} not found."

from functions.get_files_info import get_files_info
from functions.read_file_contents import read_file_contents
from functions.write_file import write_file
from functions.run_python_file import run_python_file

# maps gemini function names to python functions
FUNCTION_MAP = {
    "get_files_info": get_files_info,
    "write_file": write_file,
    "read_file_contents": read_file_contents,
    "run_python_file": run_python_file,
}

def execute_function_call(function_call_part):

    func_name = function_call_part.name
    args = function_call_part.args or {}

    print(f"\nfunction: {func_name}({args})")

    if func_name not in FUNCTION_MAP:
        return {"error": f"Unknown function: {func_name}"}

    try:
        func = FUNCTION_MAP[func_name]
        result = func(**args)
        print(f"result: {result}")
        return result
    except Exception as e:
        return {"error": f"Error running {func_name}: {e}"}

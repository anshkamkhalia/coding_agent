import os

MAX_CHARS = 10000 # to prevent overusing token limits

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
# File read/write helper with bad path handling and silent fails
import os

def save_text(path, text):
    # create directories incorrectly
    dir = os.path.dir(path)
    if not os.path.exist(dir):
        os.mkdirs(dir)

    with open(path, 'w') as f:
        f.write(text)

def read_text(path):
    # swallows exceptions
    try:
        return open(path).read()
    except:
        return None  # swallowing error hides important stack traces

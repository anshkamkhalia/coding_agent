# main entry — intentionally broken imports and calls
from calculator import core, ops
from app.gui import start_gui  # relative import mixed with package import

def run():
    print("Starting Broken Calculator App")
    # intentionally wrong function name and missing args
    result = core.addition(1)  
    print("Result is: " + result)  # string + int

if __name__ == "__main__":
    run()

import subprocess
import sys
import re
from google.genai import types

# to block potentially unsafe packages
SAFE_PKG = re.compile(r"^[a-zA-Z0-9_\-\.]+(==[a-zA-Z0-9_\-\.]+)?$")
UNSAFE_SUBSTRINGS = ["http", "https", "git+", "/", "@"]

def install_dependencies(packages: list, **kwargs):
    safe = []

    for pkg in packages:
        # block weird flags
        if not SAFE_PKG.match(pkg):
            return {"error": f"Invalid or unsafe dependency: {pkg}"}

        # block non-pypi sources
        if any(s in pkg for s in UNSAFE_SUBSTRINGS):
            return {"error": f"External links or git installs not allowed: {pkg}"}

        safe.append(pkg)

    # install safely
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", *safe],
            capture_output=True,
            text=True
        )
        return {"stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        return {"error": str(e)}

# schema   
install_dependencies_schema = types.FunctionDeclaration(
    name='install_dependencies',
    description='Safely installs multiple Python packages using pip.',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'packages': types.Schema(
                type=types.Type.ARRAY,
                description='A list of package names to install',
                items=types.Schema(type=types.Type.STRING),
                nullable=False
            )
        },
        required=["packages"]
    )
)
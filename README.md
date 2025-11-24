# AI Coding Agent

This project implements an AI coding agent built using Google's Gemini API. The agent is designed to assist users with various coding tasks by interacting with the file system and executing Python scripts within a restricted working directory.

## Features:

*   **File System Interaction**: The agent can list directory contents (`get_files_info`), read file contents (`read_file_contents`), and write to files (`write_file`).
*   **Python Script Execution**: It can execute Python files (`run_python_file`), providing output from `STDOUT` and `STDERR`.
*   **Secure Environment**: All file operations are restricted to a defined `WORKING_DIRECTORY` for security purposes.
*   **Iterative Processing**: The agent processes user prompts iteratively, making function calls based on the prompt and updating the conversation history with the results.

## How it works:

The `main.py` script initializes the Gemini client and defines the available tools (functions) the agent can use. It constructs a system prompt to guide the agent's behavior and then enters a loop to process user input. In each iteration, the agent generates a response based on the current message history and the available tools. If the response contains function calls, these calls are executed, and their results are appended to the message history for subsequent turns.

> This README was generated using the model's capability to read and access files.
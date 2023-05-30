import openai
import os
import re

# Replace with your OpenAI API key
openai.api_key = ""

def generate_code(task_description):
    prompt = f"Create a Python script that accomplishes the following task: {task_description}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI code assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    message = response['choices'][0]['message']
    if message['role'] == 'assistant':
        content = message['content']
        # Filter out everything before the first block of Python code
        match = re.search(r'```python([\s\S]*?)```', content)
        if match:
            code = match.group(1)
        else:
            code = ""
    else:
        code = ""
    return code.strip()

def main():
    action = input("Do you want to create a new script or update an existing one? Enter 'new' or 'update': ")
    task_description = input("Enter the description of the task you want to accomplish: ")

    code = generate_code(task_description)

    if action.lower() == 'new':
        script_name = input("Enter the name for the new script (without .py): ")
        script_path = f"{script_name}.py"
        mode = 'w'
        message = f"Script created: {script_path}"
    else:  # 'update'
        script_path = input("Enter the path of the script you want to update (ensure it's a .py file): ")
        if not script_path.endswith('.py'):
            script_path += '.py'
        mode = 'a'
        message = f"Script updated: {script_path}"
    
    # For debugging: print the content of the existing file before appending
    if mode == 'a':
        with open(script_path, 'r') as script_file:
            print("\nContent of the existing file before appending:\n")
            print(script_file.read())

    with open(script_path, mode) as script_file:
        if mode == 'a':
            script_file.write("\n\n# Generated code\n")
        script_file.write(code)

    print(message)

    # For debugging: print the content of the file after appending
    if mode == 'a':
        with open(script_path, 'r') as script_file:
            print("\nContent of the file after appending:\n")
            print(script_file.read())

if __name__ == "__main__":
    main()

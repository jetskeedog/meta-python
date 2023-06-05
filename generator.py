import openai
import os
import re
import subprocess

# Replace with your OpenAI API key
openai.api_key = ""

def generate_code(task_description, existing_code=None, temperature=0.5, max_tokens=300):
    if existing_code:
        prompt = f"Given the following Python script: \n\n```python\n{existing_code}\n```\n\nUpdate it to accomplish the following task: {task_description}"
    else:
        prompt = f"Create a Python script that accomplishes the following task: {task_description}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI code assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
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

    adjust_settings = input("Do you want to adjust the settings for temperature and tokens? (yes/no): ")
    if adjust_settings.lower() == "yes":
        temperature = float(input("Enter the temperature (a number between 0 and 1, inclusive): "))
        max_tokens = int(input("Enter the maximum number of tokens (an integer): "))
    else:
        temperature = 0.5
        max_tokens = 300

    existing_code = None
    if action.lower() == 'update':
        script_path = input("Enter the path of the script you want to update (ensure it's a .py file): ")
        if not script_path.endswith('.py'):
            script_path += '.py'
        with open(script_path, 'r') as script_file:
            existing_code = script_file.read()
    
    original_code = existing_code
    code = generate_code(task_description, existing_code, temperature, max_tokens)

    if action.lower() == 'new':
        script_name = input("Enter the name for the new script (without .py): ")
        script_path = f"{script_name}.py"
        message = f"Script created: {script_path}"
    else:  # 'update'
        message = f"Script updated: {script_path}"
    
    with open(script_path, "w") as script_file:
        script_file.write(code)

    print(message)

    try:
        subprocess.run(["python3", script_path], check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the script.")
        print("Error message: ", e)
        debug = input("Do you want to debug and regenerate the script? (yes/no): ")
        if debug.lower() == "yes":
            error_message = str(e)
            task_description += f". The following error occurred: {error_message}"
            existing_code = original_code
            code = generate_code(task_description, existing_code, temperature, max_tokens)
            with open(script_path, "w") as script_file:
                script_file.write(code)
            print("Script regenerated with debugging info: ", script_path)

if __name__ == "__main__":
    main()

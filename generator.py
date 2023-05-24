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
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
    )
    code = response.choices[0].message['content'].strip()
    return code

def main():
    task_description = input("Enter the description of the app you want to create: ")
    app_name = input("Enter the name for the new app (without .py): ")

    code = generate_code(task_description)
    
    with open(f"{app_name}.py", "w") as app_file:
        app_file.write(code)

    print(f"App created: {app_name}.py")

if __name__ == "__main__":
    main()

# Meta-Python

This repository contains a Python script that generates code based on a task description using the OpenAI GPT-3.5 Turbo model. 

## Prerequisites
Before using this script, you need to have an OpenAI API key. If you don't have one, sign up on the OpenAI website and obtain your API key.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Meta-Python.

```bash
pip install foobar
```

## Update API Key

```
genreator.py

# Replace with your OpenAI API key
openai.api_key = ""
```
## Usage
Run the script by executing the following command:
```
python3 generator.py
```
You will be prompted to enter the description of the app you want to create and the name for the new app. Provide the necessary inputs and press Enter.

The script will generate Python code based on the provided task description using the OpenAI GPT-3.5 Turbo model. It will create a new Python file with the specified name (app name) and write the generated code into it.

After the execution, you will see a message indicating that the app has been successfully created.
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

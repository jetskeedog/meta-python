# Meta-Python

Meta-Python is an automated Python script creator that derives instruction from user-inputted text prompts. It leverages the advanced capabilities of the OpenAI GPT-3.5 Turbo model for its operations.

## Features
* Generate Python scripts using Natural Language Processing
* Quickly Update existing Python scripts 
* Adjust script generation settings like temperature and token limit for custom needs
* Execute scripts immediately after creation or update
* Debug and regenerate scripts if any errors are encountered

## Prerequisites
Before using this script, you need to have an OpenAI API key. If you don't have one, sign up on the OpenAI website and obtain your API key.

## Installation
### Windows:
1. Ensure you have Python 3.7 or later installed. You can download it from the official site.
2. Clone this repository:
```
git clone https://github.com/jetskeedog/meta-python.git
```
3. Navigate to the directory and install the necessary Python packages:
```
cd meta-python
pip install -r requirements.txt
```
### Mac:
1. Ensure you have Python 3.7 or later installed. If not, install it using Homebrew:
```
brew install python3
```
2. brew install python3:
```
git clone https://github.com/jetskeedog/meta-python.git)
```
3. Navigate to the directory and install the necessary Python packages:
```
cd meta-python
pip3 install -r requirements.txt
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

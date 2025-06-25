import streamlit as st
import openai
import re
import subprocess
import tempfile
import os

# ——— AI code generation function ———
def generate_code(task_description, existing_code=None, temperature=0.5, max_tokens=300):
    if existing_code:
        prompt = (
            f"Given the following Python script:\n\n```python\n{existing_code}\n```\n\n"
            f"Update it to accomplish the following task: {task_description}"
        )
    else:
        prompt = f"Create a Python script that accomplishes the following task: {task_description}"
    
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI code assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    content = resp.choices[0].message.content
    m = re.search(r'```python([\s\S]*?)```', content)
    return m.group(1).strip() if m else content.strip()


# ——— Streamlit layout ———
st.title("🛠️ AI-Powered Python Script Generator")

# API Key
openai.api_key = st.sidebar.text_input(
    "OpenAI API Key", type="password", help="Your OpenAI API key"
)

# Settings
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5, 0.05)
max_tokens = st.sidebar.slider("Max Tokens", 64, 2048, 300, 64)

# Choose action
action = st.radio("What do you want to do?", ["Create new script", "Update existing script"])

# Task description
task_description = st.text_area("Describe the task you want the AI to perform", height=100)

# Upload or paste existing code if updating
existing_code = None
if action.startswith("Update"):
    uploaded = st.file_uploader("Upload your existing `.py` file", type="py")
    if uploaded:
        existing_code = uploaded.read().decode("utf-8")
    else:
        existing_code = st.text_area(
            "Or paste your existing Python code here", height=200
        )

# Generate button
if st.button("🚀 Generate Code"):
    if not openai.api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif not task_description.strip():
        st.error("Please provide a description of the task.")
    else:
        with st.spinner("Generating…"):
            code = generate_code(task_description, existing_code, temperature, max_tokens)
        st.success("Done!")
        st.code(code, language="python")

        # Offer download
        default_name = "script.py" if action.startswith("Create") else uploaded.name if uploaded else "updated_script.py"
        st.download_button(
            "💾 Download script",
            code,
            file_name=default_name,
            mime="text/plain"
        )

        # Optionally run the script
        if st.checkbox("Run this script now"):
            # write to temp file
            tf = tempfile.NamedTemporaryFile(suffix=".py", delete=False)
            tf.write(code.encode("utf-8"))
            tf.flush()
            tf.close()
            try:
                result = subprocess.run(
                    ["python3", tf.name],
                    capture_output=True, text=True, check=True
                )
                st.subheader("Output")
                st.text(result.stdout or "(no output)")
                if result.stderr:
                    st.subheader("Errors / Warnings")
                    st.text(result.stderr)
            except subprocess.CalledProcessError as e:
                st.subheader("❌ Execution failed")
                st.text(e.stderr or str(e))
            finally:
                os.unlink(tf.name)
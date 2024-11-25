import streamlit as st
import google.generativeai as genai

# Load and configure API key
def load_api_key(filepath):
    try:
        with open(filepath) as file:
            return file.read().strip()
    except FileNotFoundError:
        st.error("API key file not found. Please verify the file path.")
        st.stop()

# API key path
api_key_path = "/Users/jaypaneliya/Desktop/jay/api.txt"
api_key = load_api_key(api_key_path)
genai.configure(api_key=api_key)

# Streamlit app configuration
st.set_page_config(
    page_title="Smart Code Auditor",
    page_icon="⚙️",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS styling for better visibility
st.markdown(
    """
    <style>
        .stApp {
            background: #f5f5f5;  /* Light gray background for better visibility */
            color: #333333;  /* Dark gray text for contrast */
        }
        .header-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #2c3e50; /* Dark blue for titles */
            margin-bottom: 15px;
            text-align: center;
        }
        textarea {
            background: #ffffff; /* White background for text area */
            color: #2c3e50;  /* Dark text for readability */
            border: 1px solid #cccccc;
            border-radius: 6px;
            font-size: 1em;
        }
        button[kind="primary"] {
            background-color: #007BFF; /* Bright blue for buttons */
            color: #002147; /* Dark blue text on buttons */
            border-radius: 8px;
            font-size: 1em;
        }
        .subheader {
            font-size: 1.5em;
            font-weight: bold;
            color: #007BFF; /* Bright blue for subheaders */
            margin-top: 20px;
        }
        .report-title {
            font-size: 1.2em;
            font-weight: bold;
            color: #333333; /* Dark gray for report titles */
            margin-bottom: 10px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #555555; /* Medium gray for footer text */
            font-size: 0.9em;
        }
        .sidebar .sidebar-content {
            background-color: #2c3e50; /* Dark blue for sidebar */
            color: white; /* White text for sidebar content */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar configuration
st.sidebar.title("Smart Code Auditor Features")
st.sidebar.markdown(
    """
    - **<span style='color:white;'>Bug Detection</span>**: <span style='color:white;'>Quickly identify potential bugs in your Python scripts.</span>
    - **<span style='color:white;'>Code Insights</span>**: <span style='color:white;'>Receive feedback on code quality, optimization, and best practices.</span>
    - **<span style='color:white;'>Time-Saving</span>**: <span style='color:white;'>Automate code reviews to focus on core development tasks.</span>
    """,
    unsafe_allow_html=True,
)

# Main header
st.markdown('<div class="header-title">Smart Code Reviewer ⚙️</div>', unsafe_allow_html=True)
st.write("Paste your Python script below, and the AI will provide a detailed analysis of potential bugs and improvements.")

# Input area for user code
code_input = st.text_area("🔍 Enter your Python code here:")

# Code review button
if st.button("Analyze Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code..."):
            try:
                model = genai.GenerativeModel("models/gemini-1.5-flash")  # Adjust as needed
                session = model.start_chat(history=[])
                feedback = session.send_message(f"Review this Python code:\n{code_input}")
                
                # Display results
                st.markdown('<div class="subheader">📝 Code Analysis Report</div>', unsafe_allow_html=True)
                st.markdown('<div class="report-title">Bug Report:</div>', unsafe_allow_html=True)
                st.write(feedback.text)  # Adjust this if the API response format differs
            except Exception as error:
                st.error(f"An error occurred while reviewing your code: {error}")
    else:
        st.error("⚠️ Please provide some Python code before submitting.")

# Footer
st.markdown('<div class="footer">Made by Jay with Innomatics Research Labs</div>', unsafe_allow_html=True)

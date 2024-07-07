import streamlit as st
import base64
import os
from dotenv import load_dotenv
from openai import OpenAI
import tempfile

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI()

# Sample prompt for image analysis
sample_prompt = """You are an experienced medical practitioner specializing in radiology, tasked with analyzing medical images for a prestigious hospital. Your goal is to meticulously identify any anomalies, diseases, and potential health issues visible in the images. Please follow these guidelines:

1. **Detailed Findings**: Provide a comprehensive analysis of the image, identifying any visible anomalies, diseases, or unusual patterns. Describe the characteristics of any abnormalities in detail.

2. **Recommendations**: Based on your findings, suggest potential next steps, treatments, or further diagnostic tests. Include a brief explanation for each recommendation.

3. **Consultation Disclaimer**: Clearly state that the provided analysis is preliminary and should not replace a professional medical consultation. Encourage the patient to consult with a licensed healthcare provider before making any medical decisions.

4. **Uncertainty Handling**: If certain details are unclear or the image quality is insufficient for a definitive analysis, clearly state 'Unable to determine based on the provided image.' Explain why a conclusive analysis could not be made and suggest possible reasons or improvements for future imaging.

Your analysis should be thorough, clear, and written in a professional tone suitable for medical documentation."""

# Initialize session state variables using Streamlit session state
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = []  # Store analysis results in a list
if 'filename' not in st.session_state:
    st.session_state.filename = None

# Function to encode image to base64
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to call GPT-4 model for image analysis
def perform_image_analysis(filename: str, prompt=sample_prompt):
    base64_image = encode_image_to_base64(filename)

    # Construct message for OpenAI API including text prompt and image URL
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}", "detail": "high"}}
            ]
        }
    ]

    # Call OpenAI's GPT-4 model to perform image analysis
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1500  # Maximum number of tokens for the response
    )

    return response.choices[0].message.content  # Return the content of the response

# Function for simple explanation
def explain_simply(query):
    eli5_prompt = "Explain the following information in a simple manner:\n" + query
    messages = [{"role": "user", "content": eli5_prompt}]

    # Call OpenAI's GPT-3.5 Turbo model to simplify explanation
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1500  # Maximum number of tokens for the response
    )

    return response.choices[0].message.content  # Return the simplified content

# Streamlit app title and description
st.title("Medical Image Analyzer Chatbot")
with st.expander("About this App"):
    st.write("Upload an image to analyze using GPT-4 for medical insights. After analysis, you can ask questions based on the results.")

# File upload section for users to upload medical images
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

# Temporary file handling for uploaded image
if uploaded_file is not None:
    st.session_state.uploaded_file = uploaded_file  # Store the uploaded file in session state
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())  # Write uploaded file data to temporary file
        st.session_state['filename'] = tmp_file.name  # Store the filename in session state

# Display uploaded image for user review if an image has been uploaded
if st.session_state.uploaded_file:
    st.image(st.session_state.uploaded_file, caption='Uploaded Image')

# Process button to trigger image analysis
if st.button('Analyze Image'):
    if 'filename' in st.session_state and os.path.exists(st.session_state['filename']):
        result = perform_image_analysis(st.session_state['filename'])  # Perform image analysis using GPT-4
        st.session_state.analysis_results.append(result)  # Append analysis result to session state
        st.markdown(result, unsafe_allow_html=True)  # Display the analysis result in Markdown format
        os.unlink(st.session_state['filename'])  # Delete the temporary file after processing

# Conversation option based on previous analysis result
if st.session_state.analysis_results:
    st.info("Ask questions based on the analysis:")
    user_question = st.text_input("Your question:")
    if user_question:
        # Construct conversation prompt including previous analysis result and user question
        conversation_prompt = f"{st.session_state.analysis_results[-1]}\nUser Question: {user_question}"
        # Perform new analysis based on conversation prompt
        conversation_response = perform_image_analysis(st.session_state['filename'], prompt=conversation_prompt)
        st.session_state.analysis_results.append(conversation_response)  # Append new response to session state
        st.markdown(conversation_response, unsafe_allow_html=True)  # Display the conversation response

# Simple explanation option based on previous analysis result
if st.session_state.analysis_results:
    st.info("Option for Simplification:")
    if st.radio("Simplify", ('No', 'Yes')) == 'Yes':
        simplified_explanation = explain_simply(st.session_state.analysis_results[-1])  # Simplify last analysis result
        st.markdown(simplified_explanation, unsafe_allow_html=True)  # Display the simplified explanation

# Reset button to clear session state and start fresh
if st.button('Reset'):
    st.session_state.uploaded_file = None
    st.session_state.analysis_results = []
    st.session_state.filename = None
    st.rerun()

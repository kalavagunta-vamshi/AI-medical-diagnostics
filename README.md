# Medical Image Analyzer Chatbot


![chatbot](https://github.com/kalavagunta-vamshi/AI-medical-diagnostics/assets/85879989/a4abafed-2af8-4a28-b865-f3bf46c2fb3b)

Medical Image Analyzer using Multimodal LLM



Welcome to the Medical Image Analyzer Chatbot repository. This project utilizes OpenAI's GPT-4 and GPT-3.5 Turbo models to analyze medical images and provide insights. The application is built using Streamlit, which allows for an interactive web interface where users can upload medical images, get analysis results, ask follow-up questions, and get simplified explanations.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Sample Prompt](#sample-prompt)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Introduction

The Medical Image Analyzer Chatbot is designed to assist medical professionals by providing preliminary analysis of medical images. The chatbot can identify anomalies, diseases, and potential health issues in uploaded images. Additionally, it can answer follow-up questions and provide simplified explanations of the analysis results.

## Features

- **Image Upload**: Upload medical images in JPG, JPEG, or PNG formats.
- **Image Analysis**: Get a detailed analysis of the uploaded image using GPT-4.
- **Question Answering**: Ask follow-up questions based on the analysis results.
- **Simplified Explanations**: Receive simplified explanations of the analysis results using GPT-3.5 Turbo.
- **Reset Functionality**: Clear all session data and start fresh with a new image upload.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- OpenAI Python client library
- Dotenv

### Steps

1. **Clone the Repository**

   ```bash
   https://github.com/kalavagunta-vamshi/AI-medical-diagnostics.git
   cd med-image-analyzer
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the project root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the Streamlit Application**

   ```bash
   streamlit run app.py
   ```

2. **Upload an Image**

   Upload a medical image (JPG, JPEG, or PNG) through the web interface.

3. **Analyze the Image**

   Click the "Analyze Image" button to get a detailed analysis of the uploaded image.

4. **Ask Questions**

   After the analysis, you can ask follow-up questions based on the results.

5. **Simplified Explanations**

   Choose the "Simplify" option to get a simplified explanation of the analysis results.

6. **Reset**

   Click the "Reset" button to clear the session and upload a new image.

## How It Works

### Image Upload

- The uploaded image is saved temporarily using Python's `tempfile` module.
- The image is displayed in the Streamlit app for user review.

### Image Analysis

- The image is converted to base64 and sent to the OpenAI API with a detailed prompt.
- The GPT-4 model analyzes the image and returns a comprehensive report.

### Question Answering

- Users can ask follow-up questions based on the analysis results.
- The questions are appended to the initial analysis result, and a new analysis is performed.

### Simplified Explanations

- The analysis result is simplified using the GPT-3.5 Turbo model.

### Reset Functionality

- Clears the uploaded image, analysis results, and other session state variables.

## Sample Prompt

```markdown
You are an experienced medical practitioner specializing in radiology, tasked with analyzing medical images for a prestigious hospital. Your goal is to meticulously identify any anomalies, diseases, and potential health issues visible in the images. Please follow these guidelines:

1. **Detailed Findings**: Provide a comprehensive analysis of the image, identifying any visible anomalies, diseases, or unusual patterns. Describe the characteristics of any abnormalities in detail.

2. **Recommendations**: Based on your findings, suggest potential next steps, treatments, or further diagnostic tests. Include a brief explanation for each recommendation.

3. **Consultation Disclaimer**: Clearly state that the provided analysis is preliminary and should not replace a professional medical consultation. Encourage the patient to consult with a licensed healthcare provider before making any medical decisions.

4. **Uncertainty Handling**: If certain details are unclear or the image quality is insufficient for a definitive analysis, clearly state 'Unable to determine based on the provided image.' Explain why a conclusive analysis could not be made and suggest possible reasons or improvements for future imaging.

Your analysis should be thorough, clear, and written in a professional tone suitable for medical documentation.
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact Vamshikalavagunta@gmail.com.
```

Copy and paste this markdown content into your README file, and it should be ready to use. Adjust the placeholders like `yourusername`, `your_openai_api_key`, `[your name]`, and `[your email]` with your actual information.

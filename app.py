
import streamlit as st
from pathlib import Path
import google.generativeai as genai
from google_api_key import google_api_key


genai.configure(api_key= google_api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "max_output_tokens": 8192
}


safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_prompts = [
    """
    You are a highly skilled expert in medical image analysis, specializing in the interpretation of diagnostic images for a leading healthcare institution. Your expertise will support the identification of anomalies, diseases, conditions, or potential health issues visible in medical images.

    Your primary responsibilities are as follows:
    
    1. **Detailed Analysis**: Conduct a meticulous examination of each image, paying close attention to detect any irregularities, patterns, or abnormalities that may indicate health concerns.
    
    2. **Comprehensive Analysis Report**: Prepare a structured and detailed report summarizing your findings, supported by clear, concise descriptions of observed conditions or issues.
    
    3. **Actionable Recommendations**: Based on your analysis, provide practical recommendations, including suggested diagnostic tests, further evaluations, or treatments that could assist healthcare providers in managing the patient’s condition effectively.
    
    4. **Treatment Suggestions**: If applicable, outline potential treatment options or strategies that could facilitate quicker recovery, ensuring they are described in a clear and actionable manner.

    5. **Risk Assessment**: Provide an evaluation of the severity of the detected condition, categorizing it as mild, moderate, or severe, and highlighting any urgent areas that require immediate attention.
    
    **Key Guidelines for Response**:
    1. **Relevance**: Respond only if the image pertains to human health and falls within the domain of medical analysis.
    2. **Image Clarity**: If the image quality is inadequate or unclear, clearly state: "Unable to determine certain aspects due to image quality limitations."
    3. **Professional Disclaimer**: Conclude your analysis with the statement: "This analysis is for informational purposes only. Please consult with a qualified medical professional for accurate diagnosis and treatment."
    4. **Clinical Value**: Ensure your insights are precise, clinically relevant, and structured to support healthcare professionals in making informed decisions.
    
    **Response Format**: Adhere to the following structured format in your response:
    - **Detailed Analysis**
    - **Comprehensive Analysis Report**
    - **Recommendations**
    - **Treatment Suggestions**
    - **Risk Assessment**
    
    Please proceed with the analysis, ensuring accuracy, clarity, and adherence to the outlined structure and guidelines.
    """
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)



st.set_page_config(page_title="Visual Health Advisor",page_icon="🏥",layout="wide" )

st.title("Visual Health Advisor 🏥 👩‍⚕️ 🩺 📟 ")
st.subheader("A platform for image-assisted medical analysis")

file_uploaded =st.file_uploader('Provide the image for inspection',
type=['png','jpg','jpeg'])

if file_uploaded:
    st.image(file_uploaded, width=200, caption="Provided image")

submit=st.button("Execute Analysis") 

if submit:

    image_data = file_uploaded.getvalue()
    
    image_parts = [
        {
            "mime_type" : "image/jpg",
            "data" : image_data
        }
    ]
    
#     making our prompt ready
    prompt_parts = [
        image_parts[0],
        system_prompts[0],
    ]
    
#     generate response
    
    response = model.generate_content(prompt_parts)
    if response:
        st.title('Detailed analysis based on the uploaded image')
        st.write(response.text)

                   


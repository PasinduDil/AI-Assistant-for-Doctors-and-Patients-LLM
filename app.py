# import modeles
import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_key import api_key

#configure genai with api key
genai.configure(api_key=api_key)

#setup the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

#apply safety Settings
safety_settings=[
    {
        "category":"HARM_CATEGORY_HARASSMENT",
        "threshold":"BLOCK_MRDIUM_AND_ABOVE"
    },
    {
        "category":"HARM_CATEGORY_HATE_SPEECH",
        "threshold":"BLOCK_MRDIUM_AND_ABOVE"
    },
    {
        "category":"HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold":"BLOCK_MRDIUM_AND_ABOVE"
    },
    {
        "category":"HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold":"BLOCK_MRDIUM_AND_ABOVE"
    },



]


system_prompt=""""""
#model configuration
model = genai.GenerativeModel(model_name="gemini-pro-vision",
                            generation_config=generation_config,
                            safety_settings=safety_settings)



# set the page configuration
st.set_page_config(page_title="VitalImage Analytics",page_icon=":Robot:")

#set the logo

st.image("Image/Image.png",width=100)

# Set the title

st.title("Madicle Data Analytis")

#set the sub header
st.subheader("An application that can help users to identify medical image")
upoloaded_file=st.file_uploader("Upload as medical image for analysis",type=["png","jpg","jpeg"])
submit_button=st.button("Genarate the Analysis")

if submit_button:
    #process the uploaded image
    image_data = uploaded_file.getvalue()

    image_parts=[
        {
            "mime_type":"image/jpeg",
            "data":image_data
        },


    ]

    prompt_parts=[
        image_parts[0],
        "\n\nWhat is going on in this particular image?"


    ]
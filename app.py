# import modeles
import streamlit as st
from pathlib import Path
import google.generativeai as genai

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
    pass
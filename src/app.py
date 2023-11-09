import streamlit as st
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY") 

st.title("DALL-E Image Generator")

with st.form("images_form"):
    text = st.text_input("Enter Text Prompt")
    num_images = st.number_input("Number of Images to Generate", min_value=1, max_value=10, value=1)
    image_size = st.selectbox("Image Size (Select from Options Below)", ["1024x1024", "1024x1792", "1792x1024"], index=0)
    submit_button = st.form_submit_button(label="Generate Image")

    if submit_button:
        st.write("Generating Image...")
        response = openai.images.generate(
            model="dall-e-3",
            prompt=text,
            size=image_size,
            n=num_images
        )
        for i in range(num_images):
            url = response.data[i].url
            st.image(url, caption=f"Imagen {i+1}", use_column_width=True)

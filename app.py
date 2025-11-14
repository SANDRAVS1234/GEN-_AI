import streamlit as st
import replicate
import os

# Set your API key
os.environ["REPLICATE_API_TOKEN"] = "YOUR_API_KEY_HERE"

st.set_page_config(page_title="Interior Design Generator", layout="centered")

st.title("🏡 Text-to-Interior Generator (FLUX Schnell)")
st.write("Generate photorealistic interior designs from text prompts.")

prompt = st.text_area(
    "Enter your room description:",
    placeholder="Example: Modern bedroom with warm lighting and wooden textures"
)

generate = st.button("Generate Image")

if generate:
    if not prompt.strip():
        st.error("Please enter a prompt!")
    else:
        with st.spinner("Generating image..."):
            output = replicate.run(
                "black-forest-labs/flux-schnell",
                input={"prompt": prompt}
            )

            image_url = output[0]

            st.image(image_url, caption="Generated Interior", use_column_width=True)

            st.download_button(
                label="Download Image",
                data=requests.get(image_url).content,
                file_name="interior_design.png",
                mime="image/png"
            )

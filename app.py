import streamlit as st

st.set_page_config(page_title="Deepfake Detection System")

st.title("Deepfake Detection System")

uploaded_video = st.file_uploader(
    "Upload a video file",
    type=["mp4", "avi", "mov"]
)

if uploaded_video is not None:
    st.video(uploaded_video)
    st.success("Video uploaded successfully")
    st.info("Result: FAKE (demo logic)")

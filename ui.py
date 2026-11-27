import streamlit as st
from youtube_video_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered"


)

st.title("🎥AI YouTube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

video_url = st.text_input("Enter YouTube Video Link")  # string
button = st.button("Analyze Video") # True/False

if video_url and button:
    with st.spinner("Analyzing Video..."):
        response = agent.run(
            f"Analyze this video {video_url}"

        )
    st.markdown("Analysis report of video :")
    st.markdown(response.content)
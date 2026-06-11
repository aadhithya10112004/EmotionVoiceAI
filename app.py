import streamlit as st
import pandas as pd

from emotion_detector import detect_emotion
from emotion_detector import get_all_emotions

from tone_analyzer import analyze_tone
from graph_generator import create_emotion_chart
from history_manager import save_history
from voice_generator import generate_voice


st.set_page_config(
    page_title="Emotion Voice AI",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ Emotion-Based Voice Synthesis & Tone Analysis System")

st.caption(
    "AI-powered emotion detection using Transformers"
)

user_text = st.text_area(
    "Enter Text",
    height=150
)

if st.button("Analyze Emotion"):

    if user_text.strip() == "":
        st.warning("Please enter some text.")

    else:

        # Emotion Detection
        emotion, confidence = detect_emotion(user_text)

        # Save History
        save_history(
            user_text,
            emotion,
            confidence
        )

        # Tone Analysis
        tone = analyze_tone(emotion)
        generate_voice(
            user_text, 
            emotion
        )
        # All Emotions
        emotions = get_all_emotions(user_text)

        # Generate Graph
        create_emotion_chart(emotions)

        # Metrics Section
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Emotion",
                emotion.upper()
            )

        with col2:
            st.metric(
                "Confidence",
                f"{round(confidence * 100, 2)}%"
            )

        with col3:
            st.metric(
                "Energy",
                tone["energy"]
            )

        # Tone Analysis
        st.subheader("Tone Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.info(
                f"Pitch : {tone['pitch']}"
            )

        with col2:
            st.info(
                f"Speed : {tone['speed']}"
            )

        # Graph
        st.subheader(
            "Emotion Distribution"
        )

        st.image(
            "outputs/emotion_chart.png"
        )

        # History
        st.subheader(
            "Emotion History"
        )

        history = pd.read_csv(
            "history.csv"
        )

        st.dataframe(
            history,
            use_container_width=True
        )
import streamlit as st
import pandas as pd

from emotion_detector import detect_emotion
from emotion_detector import get_all_emotions

from tone_analyzer import analyze_tone
from graph_generator import create_emotion_chart

from history_manager import save_history
from statistics_manager import get_statistics
from insights_manager import get_insights

from voice_generator import generate_voice
from translator import translate_to_english
from translator import translate_from_english

from speech_ui import audio_to_text
from streamlit_mic_recorder import mic_recorder

from chatbot import generate_response


# ---------------------------------
# AVATAR
# ---------------------------------

def get_avatar(emotion):

    avatars = {
        "joy": "😊",
        "sadness": "😢",
        "anger": "😠",
        "fear": "😨",
        "surprise": "😲",
        "neutral": "😐",
        "disgust": "🤢"
    }

    return avatars.get(
        emotion.lower(),
        "😐"
    )


# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="Emotion Voice AI",
    page_icon="🎙️",
    layout="wide"
)

# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.title("🎙 Emotion Voice AI")

st.sidebar.markdown("---")

st.sidebar.write(
    "AI-Powered Emotion Detection and Voice Synthesis System"
)

st.sidebar.markdown("---")

# ---------------------------------
# TITLE
# ---------------------------------

st.title(
    "🎙 Emotion-Based Voice Synthesis & Tone Analysis System"
)

st.caption(
    "Transformer-Based Emotion Detection Dashboard"
)

# ---------------------------------
# TABS
# ---------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Analysis",
        "History",
        "Statistics",
        "Insights"
    ]
)

# ==================================================
# ANALYSIS TAB
# ==================================================

with tab1:

    st.subheader("Input Method")

    input_method = st.radio(
        "Choose Input",
        [
            "Type Text",
            "Speak"
        ]
    )

    voice_type = st.selectbox(
        "Voice Personality",
        [
            "Male",
            "Female",
            "Child",
            "Robot"
        ]
    )
    language = st.selectbox(
        "Language",
        [
            "English",
            "Tamil",
            "Hindi",
            "Telugu",
            "Malayalam"
        ]
    )

    user_text = ""
    
    if input_method == "Type Text":

        user_text = st.text_area(
            "Enter Text",
            height=150,
            placeholder="Type your text here..."
        )

    # ---------------------------------
    # VOICE INPUT
    # ---------------------------------

    else:

        st.info(
         "Click the microphone and speak."
        )

        audio = mic_recorder(
            start_prompt="🎤 Start Recording",
            stop_prompt="⏹ Stop Recording",
            key="voice_recorder"
        )

        if audio:

            st.success("Audio Received")

            st.audio(audio["bytes"])

            text = audio_to_text(
                audio["bytes"], 
                 language
            )

            if text:

                user_text = text

                st.success(
                    f"Detected Text: {text}"
                )

            else:

                st.error(
                    "Speech could not be recognized."
                )

    # ---------------------------------
    # ANALYZE BUTTON
    # ---------------------------------

    if st.button("Analyze Emotion"):

        if user_text.strip() == "":

            st.warning(
                "Please enter or record text."
            )

        else:

            # Emotion Detection

            english_text = translate_to_english(
                    user_text
                )

            emotion, confidence = detect_emotion(
                    english_text
                )

            ai_response = generate_response(
                    english_text,
                    emotion
                )
            translated_response = translate_from_english(
                    ai_response,
                    language
                )

            # Save History

            save_history(
                user_text,
                emotion,
                confidence
            )

            # Tone Analysis

            tone = analyze_tone(
                emotion
            )

            # Voice Output

            user_voice = generate_voice(
                user_text,
                emotion,
                voice_type,
                language,
                "outputs/user_voice.mp3"
            )

            ai_voice = generate_voice(
                translated_response,
                emotion,
                voice_type,
                language,
                "outputs/ai_voice.mp3"
            )

            if user_voice:

                st.subheader("Your Speech")
                st.audio(user_voice)

            if ai_voice:

                st.subheader("AI Response Voice")
                st.audio(ai_voice)


            # Emotion Graph

            emotions = get_all_emotions(
                english_text
            )

            create_emotion_chart(
                emotions
            )
            st.subheader(
              "AI Response"
            )

            st.success(
                translated_response
         )
            # Avatar

            avatar = get_avatar(
                emotion
            )

            st.subheader(
                "Emotion Avatar"
            )

            st.markdown(
                f"""
                <h1 style='text-align:center;
                font-size:100px'>
                {avatar}
                </h1>
                """,
                unsafe_allow_html=True
            )

            # Metrics

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

            # Tone

            st.subheader(
                "Tone Analysis"
            )

            c1, c2 = st.columns(2)

            with c1:

                st.info(
                    f"Pitch : {tone['pitch']}"
                )

            with c2:

                st.info(
                    f"Speed : {tone['speed']}"
                )

            st.success(
                f"Voice Personality : {voice_type}"
            )

            # Graph

            st.subheader(
                "Emotion Distribution"
            )

            st.image(
                 "outputs/emotion_chart.png",
                  width="stretch"
            )

# ==================================================
# HISTORY TAB
# ==================================================

with tab2:

    st.subheader(
        "Emotion History"
    )

    try:

        history = pd.read_csv(
            "history.csv"
        )

        st.dataframe(
             history,
             width="stretch"
       )

    except:

        st.info(
            "No history available."
        )

# ==================================================
# STATISTICS TAB
# ==================================================

with tab3:

    st.subheader(
        "Statistics Dashboard"
    )

    stats = get_statistics()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Analyses",
            stats["total"]
        )

    with col2:

        st.metric(
            "Most Common Emotion",
            str(stats["common"]).upper()
        )

    if stats["counts"] is not None:

        st.subheader(
            "Emotion Frequency"
        )

        st.bar_chart(
            stats["counts"]
        )

# ==================================================
# INSIGHTS TAB
# ==================================================

with tab4:

    st.subheader(
        "Emotion Insights Dashboard"
    )

    insights = get_insights()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Analyses",
            insights["total"]
        )

    with col2:

        st.metric(
            "Average Confidence",
            f"{insights['average']}%"
        )

    with col3:

        st.metric(
            "Most Common Emotion",
            str(insights["common"]).upper()
        )

    st.markdown("---")

    if insights["recent"] is not None:

        st.subheader(
            "Recent 10 Analyses"
        )

        st.dataframe(
            insights["recent"],
            width="stretch"
        )
        
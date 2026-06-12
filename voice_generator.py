import asyncio
import edge_tts


def generate_voice(
    text,
    emotion,
    voice_type,
    language,
    output_file
):

    # -----------------------------
    # Language + Voice Personality
    # -----------------------------

    if language == "English":

        voice_map = {

            "Male":
            "en-US-GuyNeural",

            "Female":
            "en-US-JennyNeural",

            "Child":
            "en-US-AriaNeural",

            "Robot":
            "en-US-DavisNeural"
        }

    elif language == "Tamil":

        voice_map = {

            "Male":
            "ta-IN-ValluvarNeural",

            "Female":
            "ta-IN-PallaviNeural",

            "Child":
            "ta-IN-PallaviNeural",

            "Robot":
            "ta-IN-ValluvarNeural"
        }

    elif language == "Hindi":

        voice_map = {

            "Male":
            "hi-IN-MadhurNeural",

            "Female":
            "hi-IN-SwaraNeural",

            "Child":
            "hi-IN-SwaraNeural",

            "Robot":
            "hi-IN-MadhurNeural"
        }

    elif language == "Telugu":

        voice_map = {

            "Male":
            "te-IN-MohanNeural",

            "Female":
            "te-IN-ShrutiNeural",

            "Child":
            "te-IN-ShrutiNeural",

            "Robot":
            "te-IN-MohanNeural"
        }

    elif language == "Malayalam":

        voice_map = {

            "Male":
            "ml-IN-MidhunNeural",

            "Female":
            "ml-IN-SobhanaNeural",

            "Child":
            "ml-IN-SobhanaNeural",

            "Robot":
            "ml-IN-MidhunNeural"
        }

    else:

        voice_map = {

            "Male":
            "en-US-GuyNeural",

            "Female":
            "en-US-JennyNeural",

            "Child":
            "en-US-AriaNeural",

            "Robot":
            "en-US-DavisNeural"
        }

    voice = voice_map.get(
        voice_type,
        "en-US-JennyNeural"
    )

    print("\n========== TTS ==========")
    print("Language :", language)
    print("Voice    :", voice)
    print("Type     :", voice_type)
    print("Text     :", text)
    print("=========================\n")

    # -----------------------------
    # Emotion Adjustment
    # -----------------------------

    rate = "+0%"

    if emotion == "joy":

        rate = "+15%"

    elif emotion == "sadness":

        rate = "-15%"

    elif emotion == "anger":

        rate = "+25%"

    elif emotion == "fear":

        rate = "-5%"

    elif emotion == "surprise":

        rate = "+20%"

    async def save_audio():

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate=rate
        )

        await communicate.save(
            output_file
        )

    try:

        asyncio.run(
            save_audio()
        )

        return output_file

    except Exception as e:

        print("TTS Error:", e)

        return None

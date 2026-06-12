import os
import edge_tts

def generate_voice(text, emotion, voice_type, language, output_file):

    os.makedirs("outputs", exist_ok=True)

    voice_map = {
        "English": {
            "Male": "en-US-GuyNeural",
            "Female": "en-US-JennyNeural",
            "Child": "en-US-AriaNeural",
            "Robot": "en-US-DavisNeural"
        },
        "Tamil": {
            "Male": "ta-IN-ValluvarNeural",
            "Female": "ta-IN-PallaviNeural",
            "Child": "ta-IN-PallaviNeural",
            "Robot": "ta-IN-ValluvarNeural"
        },
        "Hindi": {
            "Male": "hi-IN-MadhurNeural",
            "Female": "hi-IN-SwaraNeural",
            "Child": "hi-IN-SwaraNeural",
            "Robot": "hi-IN-MadhurNeural"
        },
        "Telugu": {
            "Male": "te-IN-MohanNeural",
            "Female": "te-IN-ShrutiNeural",
            "Child": "te-IN-ShrutiNeural",
            "Robot": "te-IN-MohanNeural"
        },
        "Malayalam": {
            "Male": "ml-IN-MidhunNeural",
            "Female": "ml-IN-SobhanaNeural",
            "Child": "ml-IN-SobhanaNeural",
            "Robot": "ml-IN-MidhunNeural"
        }
    }

    voice = voice_map.get(language, voice_map["English"]).get(
        voice_type, "en-US-JennyNeural"
    )

    # emotion-based speed
    rate = "+0%"
    if emotion == "joy":
        rate = "+15%"
    elif emotion == "sadness":
        rate = "-15%"
    elif emotion == "anger":
        rate = "+25%"
    elif emotion == "surprise":
        rate = "+20%"

    try:
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate=rate
        )

        # IMPORTANT: direct blocking save (no asyncio)
        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(communicate.save(output_file))
        loop.close()

        return output_file

    except Exception as e:
        print("TTS Error:", e)
        return None
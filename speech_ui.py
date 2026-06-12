import tempfile
import os
import subprocess

from faster_whisper import WhisperModel


model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)


def audio_to_text(audio_bytes,language):

    try:

        print("STEP 1: Audio received")

        # Save webm
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".webm"
        ) as webm_file:

            webm_file.write(audio_bytes)

            webm_path = webm_file.name

        print("STEP 2: WebM saved")
        print(webm_path)

        # Convert to wav
        wav_path = webm_path.replace(
            ".webm",
            ".wav"
        )

        subprocess.run(
            [
                "ffmpeg",
                "-i",
                webm_path,
                wav_path,
                "-y"
            ],
            capture_output=True,
            text=True
        )

        print("STEP 3: WAV created")
        print(wav_path)

        # Whisper
        print("STEP 4: Sending to Whisper")
        
        language_map = {
            "English": "en",
            "Tamil": "ta",
            "Hindi": "hi",
            "Telugu": "te",
            "Malayalam": "ml"
        }
        segments, info = model.transcribe(
            wav_path,
            beam_size=5,
            language=language_map[language]
        )

        print("Detected Language:", info.language)

        text = ""

        for segment in segments:

            text += segment.text + " "

        text = text.strip()

        print("Detected Text:", text)

        os.remove(webm_path)
        os.remove(wav_path)

        return text

    except Exception as e:

        import traceback

        print("ERROR:", str(e))
        print(traceback.format_exc())

        return f"ERROR: {str(e)}"
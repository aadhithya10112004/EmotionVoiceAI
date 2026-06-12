from faster_whisper import WhisperModel

# Load model once
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def speech_to_text(wav_path):

    try:

        print("STEP 4: Sending to Whisper")

        segments, info = model.transcribe(
            wav_path,
            beam_size=5
        )

        text = ""

        for segment in segments:
            text += segment.text + " "

        text = text.strip()

        print("Detected Text:", text)

        return text

    except Exception as e:

        print("Whisper Error:", e)

        return None
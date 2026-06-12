import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(f"\nVoice {i}")
    print("ID:", voice.id)
    print("Name:", voice.name)
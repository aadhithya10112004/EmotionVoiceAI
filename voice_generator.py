import pyttsx3


def generate_voice(text, emotion):

    engine = pyttsx3.init()

    rate = 200

    if emotion == "joy":
        rate = 220

    elif emotion == "sadness":
        rate = 140

    elif emotion == "anger":
        rate = 230

    elif emotion == "fear":
        rate = 190

    elif emotion == "surprise":
        rate = 210

    engine.setProperty("rate", rate)

    engine.say(text)

    engine.runAndWait()
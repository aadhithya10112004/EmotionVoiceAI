from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)


def detect_emotion(text):

    result = emotion_classifier(text)

    top_emotion = result[0][0]

    emotion = top_emotion["label"]

    confidence = top_emotion["score"]

    return emotion, confidence


def get_all_emotions(text):

    result = emotion_classifier(text)

    return result[0]
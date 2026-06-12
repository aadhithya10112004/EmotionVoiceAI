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
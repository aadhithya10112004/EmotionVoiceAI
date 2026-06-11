def analyze_tone(emotion):

    tone_mapping = {

        "joy": {
            "pitch": "High",
            "speed": "Fast",
            "energy": "High"
        },

        "sadness": {
            "pitch": "Low",
            "speed": "Slow",
            "energy": "Low"
        },

        "anger": {
            "pitch": "High",
            "speed": "Fast",
            "energy": "Very High"
        },

        "fear": {
            "pitch": "Medium",
            "speed": "Fast",
            "energy": "Medium"
        },

        "surprise": {
            "pitch": "High",
            "speed": "Medium",
            "energy": "High"
        },

        "neutral": {
            "pitch": "Normal",
            "speed": "Normal",
            "energy": "Normal"
        },

        "disgust": {
            "pitch": "Low",
            "speed": "Normal",
            "energy": "Medium"
        }
    }

    return tone_mapping.get(
        emotion.lower(),
        tone_mapping["neutral"]
    )


if __name__ == "__main__":

    emotion = input("Enter Emotion: ")

    tone = analyze_tone(emotion)

    print("\nTone Analysis")
    print("Pitch :", tone["pitch"])
    print("Speed :", tone["speed"])
    print("Energy:", tone["energy"])
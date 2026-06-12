import pandas as pd


def get_statistics():

    try:

        history = pd.read_csv("history.csv")

        total_analyses = len(history)

        most_common_emotion = (
            history["Emotion"]
            .value_counts()
            .idxmax()
        )

        emotion_counts = (
            history["Emotion"]
            .value_counts()
        )

        return {
            "total": total_analyses,
            "common": most_common_emotion,
            "counts": emotion_counts
        }

    except:

        return {
            "total": 0,
            "common": "N/A",
            "counts": None
        }
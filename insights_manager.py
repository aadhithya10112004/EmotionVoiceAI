import pandas as pd


def get_insights():

    try:

        df = pd.read_csv("history.csv")

        total = len(df)

        avg_confidence = round(
            df["Confidence"].mean(),
            2
        )

        common_emotion = (
            df["Emotion"]
            .value_counts()
            .idxmax()
        )

        recent = df.tail(10)

        return {
            "total": total,
            "average": avg_confidence,
            "common": common_emotion,
            "recent": recent
        }

    except:

        return {
            "total": 0,
            "average": 0,
            "common": "N/A",
            "recent": None
        }
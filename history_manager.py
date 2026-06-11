import pandas as pd
import os


def save_history(text, emotion, confidence):

    new_data = pd.DataFrame([
        {
            "Text": text,
            "Emotion": emotion,
            "Confidence": round(confidence * 100, 2)
        }
    ])

    if os.path.exists("history.csv"):

        old_data = pd.read_csv("history.csv")

        updated_data = pd.concat(
            [old_data, new_data],
            ignore_index=True
        )

        updated_data.to_csv(
            "history.csv",
            index=False
        )

    else:

        new_data.to_csv(
            "history.csv",
            index=False
        )
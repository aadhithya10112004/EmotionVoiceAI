import os
import matplotlib.pyplot as plt


def create_emotion_chart(emotions):

    # Create outputs folder if it doesn't exist
    os.makedirs(
        "outputs",
        exist_ok=True
    )

    labels = []
    scores = []

    for item in emotions:

        labels.append(
            item["label"].upper()
        )

        scores.append(
            item["score"] * 100
        )

    plt.figure(
        figsize=(8, 5)
    )

    plt.bar(
        labels,
        scores
    )

    plt.title(
        "Emotion Distribution"
    )

    plt.xlabel(
        "Emotion"
    )

    plt.ylabel(
        "Confidence (%)"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/emotion_chart.png"
    )

    plt.close()
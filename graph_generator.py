import matplotlib.pyplot as plt


def create_emotion_chart(emotions):

    labels = []
    scores = []

    for item in emotions:
        labels.append(item["label"].upper())
        scores.append(item["score"] * 100)

    plt.figure(figsize=(8, 5))

    plt.bar(labels, scores)

    plt.title("Emotion Distribution")

    plt.xlabel("Emotion")

    plt.ylabel("Confidence (%)")

    plt.tight_layout()

    plt.savefig("outputs/emotion_chart.png")

    plt.close()
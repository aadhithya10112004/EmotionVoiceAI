def generate_response(text, emotion):

    emotion = emotion.lower()

    if emotion == "joy":
        return "That's wonderful to hear. Keep building on this positive momentum."

    elif emotion == "sadness":
        return "Things may feel difficult right now, but steady progress often comes from small consistent steps."

    elif emotion == "fear":
        return "It is normal to feel concerned. Try breaking the challenge into smaller tasks and focus on one step at a time."

    elif emotion == "anger":
        return "Take a moment to understand what is causing the frustration and focus on actions you can control."

    elif emotion == "surprise":
        return "That sounds unexpected. Consider what this new information means and how you want to respond."

    else:
        return "Thank you for sharing. I understand your message and I'm here to help."
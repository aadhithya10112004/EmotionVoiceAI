from deep_translator import GoogleTranslator


def translate_to_english(text):

    try:
        return GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

    except Exception:
        return text


def translate_from_english(
    text,
    target_language
):

    language_map = {
        "English": "en",
        "Tamil": "ta",
        "Hindi": "hi",
        "Telugu": "te",
        "Malayalam": "ml"
    }

    try:
        return GoogleTranslator(
            source="en",
            target=language_map[target_language]
        ).translate(text)

    except Exception:
        return text
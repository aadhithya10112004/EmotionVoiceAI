def get_voice_settings(voice_type):

    settings = {

        "Male": {
            "rate": 180
        },

        "Female": {
            "rate": 210
        },

        "Child": {
            "rate": 250
        },

        "Robot": {
            "rate": 140
        }
    }

    return settings.get(
        voice_type,
        settings["Male"]
    )
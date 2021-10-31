import speech_recognition as sr


def recognize():
    r = sr.Recognizer()

    aufnahme = sr.AudioFile('output.wav')
    with aufnahme as source:
        audio = r.record(source)

    return r.recognize_google(audio)


# recognize()

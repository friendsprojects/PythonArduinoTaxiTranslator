import speech_recognition as sr


def speech_to_text(lang):
    r = sr.Recognizer()
    with sr.AudioFile('filename.wav') as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language=lang)
            print("Working on...")
            print(text)
        except:
            print("Sorry run again.")


speech_to_text('hi')

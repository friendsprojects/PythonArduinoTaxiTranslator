from gtts import gTTS

mytext = 'Arush is great. Lakshit is a bitch. I can see how it might be possible for a man to look down upon the ' \
         'earth and be an atheist, but I cannot conceive how a man could look up into the heavens and say there is no' \
         ' God. '

language = 'en'


def text_to_speech(text, language):
    obj = gTTS(text=text, lang=language, slow=False)
    obj.save("Welcome.mp3")
    print("Text to audio translation done...")


text_to_speech(mytext, language)

from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# sen = str(input("Say .... "))
lang_input = str(input("Input Language: "))         # input language from arduino
lang_output = str(input("Output Language: "))       # output language from arduino


# language code finder
def language(lang_find):
    # Dictionary of all the common languages in Google speech API
    switcher = {
        'Afrikaans': 'af',
        'Irish': 'ga',
        'Albanian': 'sq',
        'Italian': 'it',
        'Arabic': 'ar',
        'Japanese': 'ja',
        'Azerbaijani': 'az',
        'Kannada': 'kn',
        'Basque': 'eu',
        'Korean': 'ko',
        'Bengali': 'bn',
        'Latin': 'la',
        'Belarusian': 'be',
        'Latvian': 'lv',
        'Bulgarian': 'bg',
        'Lithuanian': 'lt',
        'Catalan': 'ca',
        'Macedonian': 'mk',
        'Chinese Simplified': 'zh-CN',
        'Malay': 'ms',
        'Chinese Traditional': 'zh-TW',
        'Maltese': 'mt',
        'Croatian': 'hr',
        'Norwegian': 'no',
        'Czech': 'cs',
        'Persian': 'fa',
        'Danish': 'da',
        'Polish': 'pl',
        'Dutch': 'nl',
        'Portuguese': 'pt',
        'English': 'en',
        'Romanian': 'ro',
        'Esperanto': 'eo',
        'Russian': 'ru',
        'Estonian': 'et',
        'Serbian': 'sr',
        'Filipino': 'tl',
        'Slovak': 'sk',
        'Finnish': 'fi',
        'Slovenian': 'sl',
        'French': 'fr',
        'Spanish': 'es',
        'Galician': 'gl',
        'Swahili': 'sw',
        'Georgian': 'ka',
        'Swedish': 'sv',
        'German': 'de',
        'Tamil': 'ta',
        'Greek': 'el',
        'Telugu': 'te',
        'Gujarati': 'gu',
        'Thai': 'th',
        'Haitian Creole': 'ht',
        'Turkish': 'tr',
        'Hebrew': 'iw',
        'Ukrainian': 'uk',
        'Hindi': 'hi',
        'Urdu': 'ur',
        'Hungarian': 'hu',
        'Vietnamese': 'vi',
        'Icelandic': 'is',
        'Welsh': 'cy',
        'Indonesian': 'id',
        'Yiddish': 'yi'
    }
    return switcher.get(lang_find, "Invalid language entered")          # return the language code


# Language Translator function converts input string from source language to destination language
def g_trans(sentence, source, destination):
    source = language(source)
    destination = language(destination)
    trans = Translator()
    trans_sentence = trans.translate(sentence, src=source, dest=destination)
    text_to_speech(trans_sentence.text, destination)
    return trans_sentence.text              # return the translate text in destination language


# Function to convert audio to text from source language
def speech_to_text(lang):
    r = sr.Recognizer()
    # with sr.AudioFile('filename.wav') as source:
    with sr.Microphone() as source:
        # reads the audio from filename.wav file (FYI the file should be in WAV format)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language=lang)
            print("Working on...")
            print("Input string: ", text)
        except:
            print("Sorry run again.")
        return text             # returns text from source language


# Function to convert text to audio in destination language
def text_to_speech(text, lang):
    obj = gTTS(text=text, lang=lang, slow=False)
    obj.save("Welcome.mp3")         # saves the audio in Welcome.mp3 file in same directory
    print("Text to audio translation done...")


# Function calling
print("Please Speak up...")
t = speech_to_text(language(lang_input))
t_sen = g_trans(t, lang_input, lang_output)
print("Output string: ", t_sen)
playsound('Welcome.mp3')

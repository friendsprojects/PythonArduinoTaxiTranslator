from os import path
from pydub import AudioSegment

src = "C:/Users/User/PycharmProjects/PythonPractice/Practice questions/transcript.mp3"
dst = "C:/Users/User/PycharmProjects/PythonPractice/Practice questions/test.mav"

sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")



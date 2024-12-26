# import pyttsx3
#
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()
from gtts import gTTS

tts = gTTS("hello",lang="de")
tts.save("tmp.mp3")

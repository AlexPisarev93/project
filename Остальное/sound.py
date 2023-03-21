from gtts import gTTS
from playsound import playsound

text_val = "Welcome to our coding school beach!"
language = "en"

obj = gTTS(text=text_val, lang=language, slow=False)

obj.save("test.mp3")
playsound("test.mp3")

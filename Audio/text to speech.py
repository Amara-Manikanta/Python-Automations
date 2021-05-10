import gtts
import os
import pyttsx3

engine=pyttsx3.init()

text='Hey Mani Activityyyyyyyyyyyyyyyyyyyyyyyyyyyy is done'
text1='Hey Mani Errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr ocurred'

list=['mani','dileep','chess']
langauge='en'

myobj=gtts.gTTS(text=text,lang=langauge,slow=False)

myobj.save('test.mp3')

os.system('test.mp3')
voices = engine.getProperty("voices")
print(voices)
engine.setProperty("voice", voices[0].id)
engine.say(text)

obj=gtts.gTTS(text=text1,lang=langauge,slow=False)
obj.save('error.mp3')
os.system('error.mp3')
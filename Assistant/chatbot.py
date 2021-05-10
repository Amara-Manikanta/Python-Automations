from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import pyttsx3
import pyautogui
import subprocess
import time
import os
import pandas as pd

# Initialize the recognizer
r = sr.Recognizer()
df=pd.read_csv('test.csv')


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    print(engine)
    engine.say(command)
    engine.runAndWait()


def autoreply(message):
#Responding to the message
    a = df['Reply'].where(df['Message'] == message.lower())
    q = a.dropna()
    s = q.to_string()
    l = s[5:]
    print(l)
    SpeakText(l)
    return l


def amazonlogin():
    uname='*******************'
    pwd='********************'
    time.sleep(1)
    pyautogui.moveTo(x=1647, y=221, duration=1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(x=1687, y=311, duration=1)
    pyautogui.click()
    time.sleep(3)
    ubutton = driver.find_element_by_xpath("//input[@name='email']")
    time.sleep(1)
    ubutton.send_keys(uname)
#password enter
    pbutton = driver.find_element_by_xpath("//input[@name='password']")
    time.sleep(1)
    pbutton.send_keys(pwd)
#login button click

    login_button = driver.find_element_by_xpath("//input[@type='submit']")
        #"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
    login_button.click()
# Loop infinitely for user to
# speak
i=1
while (1):
    i +=1
    print('entered' +  str(i))

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print(source2)
            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            if MyText == 'volume up':
                pyautogui.press('volumeup')
            elif MyText=='volume down':
                pyautogui.press('volumedown')
            elif MyText=='open calculator':
                subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            elif MyText=='close calculator':
                #subprocess.call("taskkill","/F","/IM","calc.exe")
                os.system("taskkill /f /im calc.exe")
            elif MyText == 'open notepad':
                subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            elif MyText=='close notepad':
                os.system("taskkill /f /im notepad.exe")
            elif MyText == 'run instagram bot':
                #subprocess.Popen('C:\\Users\\maamara\\PycharmProjects\\test\\venv\\Instagram Bot.py')
                subprocess.call(['python','C:\\Users\\maamara\\PycharmProjects\\test\\venv\\Instagram Bot.py'])
            elif MyText == 'exit':
                break
            elif MyText == 'play music':
                driver = webdriver.Chrome('C:\Installers\chromedriver.exe')
                driver.get("https://music.amazon.in/my/songs")
                driver.maximize_window()
                amazonlogin()
                driver.get("https://music.amazon.in/my/songs")
                time.sleep(15)
                pyautogui.moveTo(x=451, y=325, duration=1)
                pyautogui.click()
                time.sleep(2)
                pyautogui.moveTo(x=1691, y=204, duration=1)
                pyautogui.click()
            elif MyText == 'next song':
                pyautogui.moveTo(x=1045, y=225, duration=1)
                pyautogui.click()
            elif MyText == 'previous song':
                pyautogui.moveTo(x=905, y=222, duration=1)
                pyautogui.click()
            else:
                txt=MyText
                print(MyText)
                autoreply(MyText)





            #text=print("Hi Mani Did you say " + MyText)
            #text="Hi Mani Did you say "+''.join(MyText)
            #print(text)
            #SpeakText(text)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
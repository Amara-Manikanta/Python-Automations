import time
import pandas as pd
from openpyxl import load_workbook
import pyautogui
import win10toast
import smtplib
import gtts
from selenium import webdriver
import os

def amazon(message):
        if message=='play music':
            driver = webdriver.Chrome('C:\Installers\chromedriver.exe')
            time.sleep(10)

            driver.get('https://music.amazon.in/home')
            driver.maximize_window()
            time.sleep(2)
            uname='amaramanikantadilip@gmail.com'
            pwd='1156@Ismylife'
            # username enter
            hello_sign_in = driver.find_element_by_xpath("//div[@class='signIn']").click()
            time.sleep(1)
            sign_in_button= driver.find_element_by_xpath("//a[@class='signInButton']").click()
            time.sleep(2)
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
            songs_button = driver.find_element_by_xpath("//a[@title='Songs']").click()
            time.sleep(10)
            play_button = driver.find_element_by_xpath("//span[@class='headerIconContainer']").click()
            time.sleep(5)
            play_button = driver.find_element_by_xpath("//span[@title='Shuffle All']").click()
            time.sleep(5)

        elif message=='shuffle':
            play_button = driver.find_element_by_xpath("//span[@title='Shuffle All']").click()
            time.sleep(5)
        elif message == 'next song':
            next_song_button = driver.find_element_by_xpath("//span[@id='transportPlayNext']").click()
            time.sleep(5)
        elif message=='pause':
            pause_button = driver.find_element_by_xpath("//span[@title='Play and pause']").click()
            time.sleep(5)
        elif message=='previous song':
            previous_song_button = driver.find_element_by_xpath("//span[@id='transportPlayPrevious']").click()
            time.sleep(5)



import datetime
import os
import re
from shlex import quote
import sqlite3
import struct
import subprocess
import time
import webbrowser
from playsound import playsound
import eel
import pvporcupine
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat

#database connection to access data
con = sqlite3.connect("chanakya.db")
cursor = con.cursor()

# Playing assistant sound function
@eel.expose
def PlayAssistantSound():
    music_dir = "www\\assets\\audio\\starting_Sound.mp3"
    playsound(music_dir)
    
def getDate():
    today = datetime.date.today()
    date_string = today.strftime("%A, %B %d, %Y")
    speak(f"Today's date is {date_string}.")
    print(f"Today's date is {date_string}.")
    return date_string


import requests
def weather():
    
    api_key = '0JUnJzgQo34oasAeHLTCdA==6QCUALNMdHAyvlgE'
    latitude = 19.0760   # Mumbai Latitude
    longitude = 72.8777  # Mumbai Longitude
    url = f'https://api.api-ninjas.com/v1/weather?lat={latitude}&lon={longitude}'

    response = requests.get(url, headers={'X-Api-Key': api_key})

    if response.status_code == 200:
        data = response.json()
        if 'temp' in data:
            print(f"Weather for Coordinates ({latitude}, {longitude}):")
            print(f"Temperature: {data['temp']}°C")
            print(f"Humidity: {data['humidity']}%")
            print(f"Wind Speed: {data['wind_speed']} m/s")
            a=data['temp']
            if a is not None:
                speak(f"Temperature in {a} degrees Celsius.")
            else:
                speak("Sorry, I could not retrieve the weather information.")
        else:
            print("No weather data found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")


@eel.expose
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("something went wrong")
        
        
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)
    

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # # pressing shorcut key win+j
                # import pyautogui as autogui
                # autogui.keyDown("win")
                # autogui.press("J")
                # time.sleep(2)
                # autogui.keyUp("win")
                
                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("C")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()



# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
       
#         # pre trained keywords    
#         porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword)

#             # checking first keyword detetcted for not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key win+j
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("C")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#                 # pressing shorcut key win+j
#                 # import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("J")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()

#finding contacts from the database      
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a','tu', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0


#
def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)




#finding contacts from the database      
# def findContact(query):
    
#     words_to_remove = [ASSISTANT_NAME, 'make', 'a','tu', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
#     query = remove_words(query, words_to_remove)

#     try:
#         query = query.strip().lower()
#         cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#         results = cursor.fetchall()
#         print(results[0][0])
#         mobile_number_str = str(results[0][0])

#         if not mobile_number_str.startswith('+91'):
#             mobile_number_str = '+91' + mobile_number_str

#         return mobile_number_str, query
#     except:
#         speak('not exist in contacts')
#         return 0, 0


# #
# def makeCall(name, mobileNo):
#     mobileNo =mobileNo.replace(" ", "")
#     speak("Calling "+name)
#     command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
#     os.system(command)

#
def whatsApp(mobile_no, message, flag, name):
    

    if flag == 'message':
        target_tab = 20
        chanakya_message = "message send successfully to "+name

    elif flag == 'phone':
        target_tab = 15
        message = ''
        print("elif")
        chanakya_message = "calling to "+name
        #chanakya_message = "staring video call with "+name

    else:
        target_tab = 14
        message = ''
        print("else")
        chanakya_message = "staring video call with "+name


    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(chanakya_message)
# chat bot 
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response

def chatBot1(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    return response

def WishMe():
    hour = int(datetime.datetime.now().hour)
    time=datetime.datetime.now().strftime('%I:%M%p')
    speak("it's "+time)
    #print(time)
    if hour >= 5 and hour < 12:
        speak("Good Morning!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!")
    elif hour >= 18 and hour < 22:
        speak("Good Evening!!")
    else:
        speak("Good Night!!")
    speak("I am your personal AI Assistant. You can call me Jarvis or Alexa too, please tell me How can i assist or help you!!")

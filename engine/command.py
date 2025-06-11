# import pyttsx3
# import speech_recognition as sr 
# import eel
# import time

# def speak(text):
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.setProperty('rate', 125)
#     eel.DisplayMessage(text)
#     engine.say(text)
#     eel.recieverText(text)
#     engine.runAndWait()
    
    

# @eel.expose
# def takecommand():
    
#     r=sr.Recognizer()
    
#     with sr.Microphone() as source:
#         print('listening...')
#         eel.DisplayMessage('listening...')
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source)
        
#         audio = r.listen(source, 10, 6)
        
#     try:
#         print('recognizing')
#         eel.DisplayMessage('recognizing...')
#         query = r.recognize_google(audio, language='en-in')
#         print(f"user said: {query}")
#         eel.DisplayMessage(query)
#         time.sleep(2)
#     except Exception as e:
#         return ""
    
#     return query.lower()


# @eel.expose
# def allCommands(message=1):
#     if message == 1:
#         query = takecommand()
#         print(query)
#         eel.senderText(query)
#     else:
#         query = message
#         eel.senderText(query)
#     try:
#         query = takecommand()
#         print(query)
        
#         if "open" in query:
#             from engine.features import openCommand
#             openCommand(query)
            
#         elif "on youtube" in query:
#             from engine.features import PlayYoutube
#             PlayYoutube(query)
            
#         elif "send message" in query or "phone call" in query or "video call" in query:
#             from engine.features import findContact, whatsApp
#             message = ""
#             contact_no, name = findContact(query)
#             if(contact_no != 0):

#                 if "send message" in query:
#                     message = 'message'
#                     speak("what message to send")
#                     query = takecommand()
                    
#                 elif "phone call" in query:
#                     message = 'call'
#                 else:
#                     message = 'video call'
                    
#                 whatsApp(contact_no, query, message, name)
#         else:
#             print("not run")
#     except:
#         print("error")
        
        
#     eel.ShowHood()



import sys
import time
import webbrowser
import wikipedia
import datetime
import pyjokes
import pyttsx3
import speech_recognition as sr
import eel


def speak(text):
    text=str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.setProperty('rate', 174)             # setting up new voice rate
    #print(voices)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


@eel.expose
def takecommand():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening....")
        eel.DisplayMessage("listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio=r.listen(source,10,6)
    
    try:
        print("Recognizing")
        eel.DisplayMessage("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        #speak(query)
        #eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        print("Received query:", query)  # Debug statement
        
        if "open" in query:
            print("Matched 'open' condition")
            from engine.features import openCommand
            openCommand(query)
            
        elif "play" in query:
            print("Matched 'play' condition")
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif "on youtube" in query:
            print("Matched 'on youtube' condition")
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        elif "weather" in query:
            print("Matched 'wheather' condition")
            from engine.features import weather
            weather()
            
        elif "wish me" in query:
            print("Matched 'wish me' condition")
            from engine.features import WishMe
            WishMe()
            
        elif "wikipedia" in query:
            print("Matched 'wikipedia' condition")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp #makeCall ,sendMessage
            flag=""
            contact_no, name = findContact(query)
            
            if(contact_no != 0):
                if "send message" in query:
                    flag='message'
                    speak("what message to send")
                    query=takecommand()
            elif "phone call" in query:
                flag='phone'
            else:
                flag='video'
            
            whatsApp(contact_no, query, flag, name)
                
        elif "time" in query:
            print("Matched 'time' condition")
            time_now = datetime.datetime.now().strftime('%I:%M%p')
            speak("The current time is " + time_now)
        
        elif "date" in query:
            print("Matched 'date' condition")
            from engine.features import getDate
            getDate()
            
        elif "joke" in query:
            print("Matched 'joke' condition")
            joke = pyjokes.get_joke()
            speak(joke)
        
        elif "your name" in query:
            print("Matched 'your name' condition")
            from engine.config import ASSISTANT_NAME
            # speak("I am " + ASSISTANT_NAME)
            from engine.features import chatBot1
            speak("I am " + ASSISTANT_NAME +"  "+chatBot1(query))
            
        elif "stop" in query or "bye" in query:
            print("Matched 'stop' or 'bye' condition")
            sys.exit()
        
        # elif "who" in query:
        #     print("Matched 'who' condition")
        #     from engine.config import ASSISTANT_NAME
        #     a= ASSISTANT_NAME
            
        
        else:
            if query!=0:
                print("Entering chatBot block with query:", query)
                a="in 50 words"
                query=query+a
                from engine.features import chatBot
                chatBot(query)
            else:
                speak("I could not hear you properly")
                print("chatBot block executed")

    except Exception as e:
        print("Error occurred:", e)

    eel.ShowHood()
    query="Hello, I am J.A.R.V.I.S "
    eel.DisplayMessage(query)


#text = takecommand()       

#speak(text)
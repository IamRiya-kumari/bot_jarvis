'''This is a python project'''
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os.path
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
import time
import pyjokes
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5, phrase_time_limit = 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak(" Sorry Say that again please...")
        return "none"
    return query

#To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour <=12:
        speak("Good Morning")
    
    elif hour>12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    
    speak("I am jarvis ...Please tell me how can I help you")


#To send Email

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('princessarora486@gmail.com', 'Princ@127')
    server.sendmail('princessarora486@gmail.com', to, content)
    server.close()



# for news update

def news():
    main_url ="https://newsapi.org/v2/everything?q=tesla&from=2021-04-24&sortBy=publishedAt&apiKey=16b09538634446b0a12afac446c166cf"

    main_page = requests.get(main_url).json()

    #print(main_page)
    articles = main_page["articles"]

    #print(articles)
    head =[]
    day =["first","second","third","fourth", "fifth", "sixth", "seventh","eighth","ninth","tenth"]

    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        #  print(f"today's {day[i]} news is :", head[i])
        speak(f"today's {day[i]} news is : {head[i]}")


if __name__ ==  "__main__":
    wish()
    #takecommand()
    while True:
    #if 1:


        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        
        elif "open paint " in query:
            ppath ="C:\\WINDOWS\\system32\\paint.exe"
            os.startfile(ppath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k= cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir ="C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))


        elif "ip address"  in query:
            ip = get('https://api.iptify.org').text
            speak(f"your IP address is {ip}")



        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            # print(results) 

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

            
        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("Sir, what should I search on google")
            sr = takecommand().lower()
            webbrowser.open(f"{sr}")

        # elif "send Whatsapp message" in query:
        #     kit.sendwhatmsg("+917562870042","Hi I am Jarvis this is testing message", 4, 13)
        #     time.sleep(120)
        #     speak("message has been sent")

        # elif "play songs on youtube " in query:
        #     kit.playonyt("Bepanah Pyar")

        # # elif "email to riya" in query:

        #     try:
        #         speak("what should i say?")
        #         content = takecommand().lower()
        #         to = "riyakumari.rk219@gmail.com"
        #         sendEmail(to ,content)
        #         speak("Email has been sent to Riya")

        #     except Exception as e:
        #         print(e)
        #         speak("Sorry Sir, I am unable to send this email to riya")

        elif "you can sleep" in query:
            speak("Thanks for using me, have a good day.")
            sys.exit()    



#To close application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

#To set an alarm
        elif "set alarm" in query:
            nn =  int(datetime.datetime.now().hour())
            if nn == 22:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

#To find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system " in query:
            os.system("shutdown/r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        elif "tell me news" in query:
            speak("Please wait sir, fetching the latest news")
            news()


        elif "send email to Riya" in query:

            speak("Sir what should I say")

            query = takecommand().lower()
            if "send a file" in query:
                email ='princessarora486@gmail.com'
                password ='Princ@127'
                send_to_email ='riyakumari.rk816@gmail.com'
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2
                speak("Sir please enter the correct path of the file into the shell")
                file_location = input("Please enter the path here: ")

                speak("Please wait, I am sending email now")

                msg =  MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                #Setup the attachment

                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Consent-Disposition',"attachment; filename = %s " %filename)


                #attach the attachment to the MIMEMultipart object

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendemail(email, send_to_email,  text)
                server.quit()
                server("email has been sent to riya")


            else:
                email = 'princessarora486@gmail.com'
                password = 'Princ@127'
                send_to_email ='riyakumari.rk816@gmail.com'

                message = query

                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email, password)
                server.sendemail(email, send_to_email,  message)
                server.quit()
                server("email has been sent to riya")


            # To find my location using IP address

        elif "where i am" in query or "where we are" in query:
            speak("Wait , let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url ='https://get.geojs.io/vl/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                state=geo_data['state']
                country = geo_data['country']
                speak(f"Maybe I am not sure, but i Think we are in{city}city of  {state} state of country {country} ")
            except Exception as e:
                speak("Sorry, Due to network issue I am not able to find where we are.")
                pass


            #To check a instagram profile

        elif "instagram profile " in query or "profile on instagram" in query:
            speak(" Please enter the user name correctly. ")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f" Here is the profile of the user{name}")
            time.sleep(5)
            speak("Would you like to download the profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only = True)
                speak("I am done, Profile picture is saved in our main folder, now i am ready for other work ")
            else:
                pass
        



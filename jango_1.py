import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import smtplib
import pyaudio
import pyjokes
print("Intializing Jango")
MASTER = "JUNO"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning"+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("HI I am Jango How can I help you. ")
#Main program...
#will take command form mic
def takeCommant():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("Listening...")
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio  )
        print(f'user said: {query}\n')
        if 'jango' in str(query.lower()):
            query = query.replace('jango',"")
    except Exception as e:
        speak("Say that again please")
        query=None

    return query
def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gamil.com',"password")
    server.sendmail("juno@gmail.com",to,content)
    server.close()

speak('Intializing Jango....')
wishMe()
def run_jango():
    query = takeCommant()
    # Logics for execution
    if 'wikipedia' in str(query.lower()):
        speak("searching wikipedia...")
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query, sentences=2)
        speak(results)
    elif 'open youtube' in str(query.lower()):
        webbrowser.open("youtube.com")
    elif 'open reddit' in str(query.lower()):
        webbrowser.open("reddit.com")
    elif 'play music' in str(query.lower()):
        songs = os.listdir("D:\music")
        print(songs)
        os.startfile(os.path.join("D:\music", songs[0]))
    elif "the time" in str(query.lower()):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(MASTER + "time is" + strTime)
    elif 'email to harry' in str(query.lower()):
        try:
            speak("what should i send")
            content = takeCommant()
            to = "harry@gmail.com"
            sendmail(to, content)
            speak('email is sent successfully')
        except Exception as e:
            print(e)
    elif 'how are you' in str(query.lower()):
        speak('I am Fine and what about you JUNO')
        reply = takeCommant()
        if "fine" in str(reply.lower()):
            speak("Good to hear")
        else:
            speak("what happened?")
    elif 'joke' in str(query.lower()):
        speak(pyjokes.get_joke())
    else:
        speak("Please say the command again.")
while True:
    run_jango()

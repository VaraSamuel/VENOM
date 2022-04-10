from distutils.util import strtobool
import smtplib
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
import requests, json
from bs4 import BeautifulSoup
import requests
from pyaudio import PyAudio
import wave
from speech_recognition import Recognizer,AudioFile
from apiclient.discovery import build 
from os import system

Owner = "Sam"
print("Initializing Venom")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#for making Venom say its getting iinitialized !!############################

def speak(text):
    
    engine.say(text)
    engine.runAndWait()
    
speak("Initializing. Venom...Designed by Code Champs...")

#basic etiquettes for Venom like goodmorning ################################

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        
        speak("Goodmorning sir"+ Owner)
        
    elif hour>=12 and hour<18:
        
        speak("Good afternoon sir "+ Owner)
    else:
        
        speak("Good evening sir "+ Owner)
        
    speak("I am Venom. How may i help you sir?")
    
    #main use of Venom and giving input to her #################

def takecommand():
    
    
    # secret class for a speech recognition and enabling the microphone to hear you #####################
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        
        print("Recognising your beautiful voice sir...")    
        speak("Searching till the moon and back for your results sir. ")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"your querry is: {query}\n")
    except Exception as e:
        
        print("Please come again sir..")
        query = 'None'
    return query
def sendEmail(to, content):
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sanboo1969@gmail.com', 'daffodils')
    server.sendmail('sanboo1969@gmail.com', to, content)
    server.close()

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    speak(location)
    speak(time)
    speak(info)
    speak(weather+"°Centigrade")
    
    
wishme()

query = takecommand()


#logic for executing tasks as per the query ############################

if 'wikipedia' in query.lower() :
    
    speak('Searching in wikipedia...')
    
    query = query.replace("wikipedia","")
    
    result = wikipedia.summary(query,sentences = 2)
    
    speak (result)
    
elif 'open youtube' in query.lower():
    speak("Your youtube webpage is opening sir.")
    webbrowser.open("youtube.com")
    
elif 'open google' in query.lower():
    speak("Your google search engine is opening sir.")
    webbrowser.open("google.com")
    
elif 'open stack overflow' in query.lower():
    speak("Your requested site is opening sir.")
    webbrowser.open("stackoverflow.com")
    
elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"Sir, the time is {strTime}")
    
elif 'open code' in query:
    speak("Here is the visual studio front page sir.")
    codePath = "C:\\Users\\Samuel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
    
elif 'send an email' in query:
    
    try:
        speak("What should i say?")
        content = takecommand()
        to = "samuelconnery4@gmail.com"
        sendEmail(to,content)
        speak("Email has been sent sir..Please sit and relax")
        
    except Exception as e:
        print(e)
        speak("Your email has not been sent sir")

elif 'srm web page' in query.lower():
    speak("Your requested site is opening sir.")
    webbrowser.open("https://www.srmist.edu.in/")

elif "tell me a joke" in  query.lower():
    
    speak("How did the telephone propose to its girlfriend? He gave her a ring. hahahahaha.... ")
    
elif "feminism" in query.lower():
    speak("sir did you mean a book on home science.....sorry for the glitch sir")


# elif "weather" in query.lower():
#     # base URL
#     BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
#     # City Name CITY = "Hyderabad"
#     # API key API_KEY = "Your API Key"
#     # upadting the URL
#     URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
#     # HTTP request
#     response = requests.get(URL)
#     # checking the status code of the request
#     if response.status_code == 200:
#    # getting data in the json format
#         data = response.json()
#    # getting the main dict block
#         main = data['main']
#    # getting temperature
#         temperature = main['temp']
#    # getting the humidity
#         humidity = main['humidity']
#    # getting the pressure
#         pressure = main['pressure']
#    # weather report
#         report = data['weather']
#         speak(f"{CITY:-^30}")
#         speak(f"Temperature: {temperature}")
#         speak(f"Humidity: {humidity}")
#         speak(f"Pressure: {pressure}")
#         speak(f"Weather Report: {report[0]['description']}")
#     else:
#    # showing the error message
#         speak("Error in the HTTP request")
elif "weather" in query.lower():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    speak("please say the name of the required city, sir.")
    city = takecommand()
    city = city+" weather"
    weather(city)
    speak("Have a Nice Day:)")
elif "play in youtube" in query.lower():
    CHUNK = 1024
    FORMAT = 8
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 4
    WAVE_OUTPUT_FILENAME = "output.wav"
    DEVELOPER_KEY = "AIzaSyAjGsnss9-r0P_6Wrykg2tcWe_vuhcz2dE" 
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                      developerKey = DEVELOPER_KEY)
                                        
    p = PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    print("Say Something to search on Youtube")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Searching....")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    r = Recognizer()
    temp_audio = AudioFile(WAVE_OUTPUT_FILENAME)
    with temp_audio as source:
        audio = r.record(source)
    try:
        output = r.recognize_google(audio)
    except:
        print("Error Try again")
    if "play" in output:
        output.replace("play","")
        search_keyword = youtube.search().list(q = output, part = "id, snippet", 
                                               maxResults = 1).execute()
        URLS = f"https://www.youtube.com/watch?v={search_keyword['items'][0]['id']['videoId']}"
    print(URLS)
# system(f"vlc {URLS} &")
    webbrowser.open(URLS)




import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # Choose a specific voice (e.g., the second voice)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            print('recognizing')
            eel.DisplayMessage('recognizing....')
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")
            eel.DisplayMessage(query)
            time.sleep(2)
            
            return query.lower()
        except sr.WaitTimeoutError:
            print("Timed out waiting for speech input.")
            return ""
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Error connecting to Google Web API: {e}")
            return ""
        
 
@eel.expose       
def allCommands():
    
    try:
        query = takecommand()
        print(query)
        
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
            
        else:
            print("not run")
            
    except:
        print("error")
            
        eel.ShowHood()
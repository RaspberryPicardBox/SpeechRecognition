import speech_recognition as sr
import pyttsx
import os
import time
import datetime

def speak(text):
    print(text)
    engine = pyttsx.init()
    engine.say(str(text))
    engine.runAndWait()
    
def speechGoogle():                                                                    
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Input:")                                                                                   
        audio = r.listen(source)   

    try:
        speechInput = r.recognize_google(audio)
        print("Recognised: " + speechInput)
        return speechInput
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0} Using Wit.ai services".format(e))
        speechWit()
    except:
        print("Exception occured. Using Wit.ai services")
        speechWit()
            

def speechWit():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Input:")                                                                                   
        audio = r.listen(source)

        WIT_AI_KEY = "WIT KEY"

        try:
            speechInput = r.recognize_wit(audio, key=WIT_AI_KEY)
            print("Recognised: " + speechInput)
            return speechInput
        except sr.UnknownValueError:
            print("Wit.ai could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Wit.ai service; {0} Using Sphinx services".format(e))
            speechSphinx()
        except:
            print("Exception occured. Using Sphinx services")
            speechSphinx()

def speechSphinx():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Input:")                                                                                   
        audio = r.listen(source)

    try:
        speechInput = r.recognize_sphinx(audio)
        print("Recognised: " + speechInput)
        return speechInput
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    except:
        print("Complete speech recognition failure")

def recognise():
    command_words = ["shutdown", "time"]
    
    command = speechGoogle()
    if command == None:
        main()
    else:
        words = command.split()

        for word in words:
            for command_word in command_words:
                if word == command_word:
                    if word == "shutdown":
                        os.system("mpg321 /home/pi/General\ Python\ Projects/Speech\ Recognition/Sounds/end_beep.mp3 &")
                        exit()
                    elif word == "time":
                        now = datetime.datetime.now()
                        speak("The time is currently ")
                        speak(now.hour+1)
                        speak("hundred")
                        speak("and")
                        speak(now.minute)
                        speak("hours.")
                    else:
                        main()
                else:
                    main()

#---MAIN---

def main():
    while online == True:
        listen = speechGoogle()
        heard = listen.split()
        if "computer" in heard:
            print("Keyword detected")
            os.system("mpg321 /home/pi/General\ Python\ Projects/Speech\ Recognition/Sounds/beep_respond.mp3 &")
            recognise()
        else:
            main()

#---PRE-MAIN---
    
print("Loading complete...")
os.system("mpg321 /home/pi/General\ Python\ Projects/Speech\ Recognition/Sounds/start_beep.mp3 &")
online = True
main()
exit()

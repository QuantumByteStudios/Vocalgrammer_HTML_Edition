import os
import time
import pyttsx3
import speech_recognition as sr
import datetime
import platform


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


if platform.system() == "Windows":
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    userSaid = "hello world"
else:
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', 160)
    userSaid = "hello world"


# Wishing Function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

# Speak Function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Listening Function


def takecommand(wtr=0):
    r = sr.Recognizer()
    r.pause_threshold = 1
    r.operation_timeout = 5
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=5)

        try:
            print("Recognizing...\n")
            heard = r.recognize_google(audio)
            print(f"You Said: \"{heard}\"")
            return heard.lower()
        except sr.UnknownValueError:

            speak("I didnt understand what you said")
            print(
                "You said something that is beyond my understanding or maybe you didn't say anything.\n")
            engine.runAndWait()
            return 0

# Introduction Function


def introduction():
    print("Getting started without wasting your precious time...")
    speak("Welcome to VOCALGRAMMER  <HTML EDITION>, version 0.1, created by  Quantum Byte Studios and FrosT, Getting started without wasting your precious time.")

# ScilenceChecker Function Takes input and removes scilence
# def scilenceChecker():
# 	userSaid = takecommand().lower()
# 	if userSaid == "":
# 		userSaid = "nothing"
# 	elif userSaid == " ":
# 		userSaid = "nothing"
# 	else:
# 		userSaid = takecommand().lower()


def clearLog():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


creditsScreen = '''
 _____ _                 _          _____            _   _     _
|_   _| |__   __ _ _ __ | | _____  |  ___|__  _ __  | | | |___(_)_ __   __ _
  | | | '_ \ / _` | '_ \| |/ / __| | |_ / _ \| '__| | | | / __| | '_ \ / _` |
  | | | | | | (_| | | | |   <\__ \ |  _| (_) | |    | |_| \__ \ | | | | (_| |
  |_| |_| |_|\__,_|_| |_|_|\_\___/ |_|  \___/|_|     \___/|___/_|_| |_|\__, |
                                                                       |___/
CREDITS:
QuantumByteStudios
FrosT

Github{
	QuantumByteStudios:  https://github.com/QuantumByteStudios
	FrosT:				 https://github.com/FrosT2k5
}

Website{
	QuantumByteStudios:  http://quantumbyteofficial.tech/
	FrosT: 				 https://www.frost2k5.games/
}

'''

clearLog()

welcomeSplashScreen = '''

---------------------------------------------------------------------------			
		   ***
		  **/**
		 **/||**	| V O C A L G R A M M E R  <HTML EDITION>
		 **||/**	| ---------------------------------------
		  **/**		| F r o s T  &  Q u a n t u m  A I
 		   ***
---------------------------------------------------------------------------	            
	
'''

print(f"{bcolors.OKCYAN + welcomeSplashScreen + bcolors.ENDC}")

clearLog()
if __name__ == '__main__':
    introduction()
    wishMe()
    looper = 5

    while looper != 10:

        query = str(takecommand())

        # Probablity of Commands

        if "open notepad" in query:
            command = "C:\\WINDOWS\\system32\\notepad.exe"
            os.system(command)
        elif "open browser" in query:
            command = "start https://www.google.com"
            os.system(command)
        elif "clear log" in query:
            clearLog()
        elif "pause" in query:
            a = input("press any key to continue...")

        elif "add address" in query:
            speak("Adding your address, Tell me your address")
            address = input("Please type your address: ")
            finalTag = (f"<address>{address}</address>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("Address added!\n")

        elif "add attribute" in query:
            speak("adding your Attribute")
            print("Tell me the your URL")
            URL = input("Enter/Paste your URL: ")
            URLName = input("Enter tittle of your URL: ")
            finalTag = (f'<a href="{URL}">{URLName}</a>\n')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("Attribute/URL added!\n")

        elif "add audio" in query:
            speak("adding your Audio")
            print("Tell me path of your audio.")
            audioPath = input("Enter/Paste your path: ")
            finalTag = (
                f'<audio controls autoplay><source src="{audioPath}" type="audio/mpeg"></audio>\n')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("Audio added!\n")

        elif "add blockquote" in query:
            speak("adding your blockquote, Tell me your blockquote content")
            print("Say your blockquote content: ")
            query = str(takecommand())
            blockquote = query
            finalTag = (f"<blockquote>{blockquote}</blockquote>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("Comment added!\n")

        elif "add br" in query:
            speak("adding your br tag")
            finalTag = (f"<br>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("br added!\n")

        elif "add button" in query:
            speak("adding your Button")
            buttonName = input("Enter your Button name: ")
            finalTag = (f'<button type="button">{buttonName}</button>\n')
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("Attribute/URL added!\n")

        elif "add comment" in query:
            speak("adding your comment, Tell me your comment")
            print("Say your comment: ")
            query = str(takecommand())
            comment = query
            finalTag = (f"<!--{comment}-->\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("Comment added!\n")

        elif "add heading" in query:
            speak("adding your heading, Tell me your heading Size")
            print("Say your heading size: ")
            query = str(takecommand())
            sizeOfHeadingTag = query
            # sizeOfHeadingTag = input("Enter size of Heading Tag(1, 2 ,3 ,4...): ")
            # contentOfHeading = input("Enter content of Heading: ")
            speak("Adding your heading, Tell me your heading content")
            print("Say your heading content: ")
            query = str(takecommand())
            contentOfHeading = query
            finalTag = (
                f"<h{sizeOfHeadingTag}>{contentOfHeading}</h{sizeOfHeadingTag}>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("Heading added!\n")

        elif "add hr" in query:
            speak("adding your hr tag")
            finalTag = (f"<hr>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("hr added!\n")

        elif "add iframe" in query:
            speak("adding your iframe tag")
            width = input("Enter Width of your ifame in pixels: ")
            height = input("Enter height of your ifame in pixels: ")
            url = input("paste/enter url for iframe: ")
            finalTag = (
                f"<iframe src=\"{url}\" width=\"{width}px\" height=\"{height}px\"></iframe>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("iframe added!\n")

        elif "add image" in query:
            speak("adding your image tag")
            image_name = input("Enter name of your image in pixels: ")
            width = input("Enter Width of your image in pixels: ")
            height = input("Enter height of your image in pixels: ")
            url = input("paste/enter url for image with extension: ")
            finalTag = (
                f"<img src=\"{url}\" width=\"{width}px\" height=\"{height}px\" alt=\"{image_name}\">\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("image added!\n")

        # elif "add list" in query:
        # 	speak("adding your list tag (Unordered list)")
        # 	noofitems = input("Enter number of items in your list: ")
        # 	finalTag = (f"<ul>\n")
        # 	f = open("index.html", "a")
        # 	f.write(finalTag)
        # 	for i in noofitems:
        # 		user_item_input = input("Enter your item: ")
        # 		finalTag = (f"<li>{list_items}</li>\n")
        # 		f = open("index.html", "a")
        # 		f.write(finalTag)
        # 		f.close()
        # 	finalTag = (f"/ul>\n")
        # 		f = open("index.html", "a")
        # 		f.write(finalTag)
        # 	clearLog()
        # 	print("list added!\n")

        elif "add paragraph" in query:
            speak("adding your paragraph")
            print("\nNo Speech input for paragraph because paragraphs can be too long to speak\nDo not press enter for new line type \"<br>\" to change line")
            content = input("Start typing/paste your paragraph here: \n")
            finalTag = (f"<p>{content}</p>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("paragraph added!\n")

        elif "add video" in query:
            speak("adding your video tag")
            width = input("Enter Width of your video in pixels: ")
            height = input("Enter height of your video in pixels: ")
            url = input(
                "paste/enter url for video without extension (mp4 only): ")
            finalTag = (
                f"<video width=\"{width}\" height=\"{height}\" controls><source src=\"{url}.mp4\" type=\"video/mp4\"></video>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            print("video added!\n")

        elif "complete website" in query:
            speak("completing your website")
            finalTag = (f"</body>\n</html>\n")
            f = open("index.html", "a")
            f.write(finalTag)
            f.close()
            clearLog()
            speak("Website Completed!, Thanks for using VOCALGRAMMER\n")
            print("Website Completed!\n")

        elif "terminate program" in query:
            speak("ending program, thanks for using VOCALGRAMMER")
            os.system("cls")
            print(f"{bcolors.OKCYAN + creditsScreen + bcolors.ENDC}")
            print("VOCALGRAMMER ended sucessfully")
            looper = 10

        else:
            print("\n\nREQUEST ERROR\n\n")

import pyttsx3
engine = pyttsx3.init()
engine.say("This is an audio file.", "output.mp3")
engine.runAndWait()      
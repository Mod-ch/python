import pyttsx3 # type: ignore

engine = pyttsx3.init()
name = input("what is your name ? ")
engine.say(f"Hello {name}")
engine.runAndWait()
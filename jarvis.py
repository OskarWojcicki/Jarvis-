import speech_recognition as sr 
import subprocess

def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("[System]: Aha... Welcome Oskar. What do you need.")
        audio = recognizer.listen(source)

        return audio 

def recognize_speech(audio):
    recognizer = sr.Recognizer()
    try:
        print("[System]: Processing voice...")
        text = recognizer.recognize_google(audio, language="en-US")    
        return text 
    except sr.UnknownValueError:
        return "[Error]: Could not understand audio"
    except sr.RequestError:
        return "[Error]: Could not request results"

def speak(text):
    print(f"[Jarvis]: {text}")
    # Dodajemy argument "-v", a po nim nazwę angielskiego głosu (np. "Alex" lub "Samantha")
    subprocess.run(["say", "-v", "Alex", text])

def process_command(command):
    command = command.lower()

    if "hello" in command or "hi" in command or "Hej Jarwis" in command:
        speak("Welcome back Sir. All system are online. How can I help you now?")
    elif "goodbye" in command:
        speak("Goodbye Sir. Powering down systems.")
        exit()
    else:
        # speak("I heard you, but I did not understand, could you say that again")
        speak("Nie dosłyszałem cię ")

if __name__ =="__main__":

    captured_audio = listen_command()

    text_result = recognize_speech(captured_audio)
    print(f"[Result]: {text_result}")

    process_command(text_result)
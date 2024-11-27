import pyttsx3
import pyautogui
import webbrowser as wb

engine = pyttsx3.init()

def speak(text, speed=160, voice="com.apple.speech.synthesis.voice.Karen"):
    voices = engine.getProperty('voices')
    engine.setProperty('rate', speed)

    for v in voices:
        if voice in v.id:
            engine.setProperty('voice', v.id)
            break

    engine.say(text)
    engine.runAndWait()

def takeCommandMIC():
    return input("You: ")

def sendwhatsmsg(phone_no, message):
    try:
        wb.open(f'https://web.whatsapp.com/send?phone={phone_no}&text={message}')
        pyautogui.sleep(10) 
        pyautogui.press('enter') 
        speak("Message has been sent.")
    except Exception as e:
        print(f"Error: {e}")
        speak("Unable to send the message.")

if __name__ == "__main__":
    user_name = {
        'John': '+91 8652661497'
    }

    try:
        speak("To whom do you want to send the message?")
        name = takeCommandMIC().strip()

        if name in user_name:
            phone_no = user_name[name]
            speak("What is the message?")
            message = takeCommandMIC()
            sendwhatsmsg(phone_no, message)
        else:
            speak(f"Sorry, I couldn't find {name} in your contact list.")
    except Exception as e:
        print(f"Error: {e}")
        speak("Unable to send the message.")

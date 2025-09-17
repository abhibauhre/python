import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    """Greet the user based on the time of day."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you?")

def tell_time():
    """Tell the current time."""
    now = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {now}")

def search_wikipedia(query):
    """Search Wikipedia and speak the summary."""
    speak("Searching Wikipedia...")
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    except Exception:
        speak("Sorry, I could not find any results on Wikipedia.")

def open_website(url):
    """Open a website in the default browser."""
    speak(f"Opening {url}")
    webbrowser.open(url)

def play_youtube(query):
    """Play a YouTube video based on the query."""
    import pywhatkit
    speak(f"Playing {query} on YouTube")
    pywhatkit.playonyt(query)

def main():
    greet()
    while True:
        command = input("You: ").lower()

        if "time" in command:
            tell_time()
        elif "wikipedia" in command:
            query = command.replace("wikipedia", "").strip()
            search_wikipedia(query)
        elif "open" in command and "website" in command:
            speak("Which website should I open?")
            site = input("Website: ")
            if not site.startswith("http"):
                site = "https://" + site
            open_website(site)
        elif "youtube" in command or "play" in command:
            query = command.replace("play", "").replace("youtube", "").strip()
            play_youtube(query)
        elif "hello" in command or "hi" in command:
            greet()
        elif "exit" in command or "quit" in command or "bye" in command:
            speak("Goodbye! Have a nice day.")
            break
        else:
            speak("Sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()
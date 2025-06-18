import speech_recognition as sr
import pyttsx3

# Your dictionary
vernacular_dict = {
    "habari": "hello",
    "asante": "thank you",
    "karibu": "welcome",
    "chakula": "food",
    "kwaheri": "goodbye",
    "jina": "name",
    "lako": "your",
    "nani": "who",
    "nataka": "I want",
    "maji": "water",
    "mimi": "I",
    "ni": "am",
    "mwanafunzi": "student",
    "mwalimu": "teacher"
    "chamgea": "hi",
}

# Translation logic
def translate_to_english(sentence):
    words = sentence.lower().split()
    translation = []
    for word in words:
        translated = vernacular_dict.get(word, f"[{word}]")
        translation.append(translated)
    return ' '.join(translation)

# Text-to-Speech setup
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech Recognition
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak a sentence in your vernacular...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        print("Speech recognition service error.")
        return ""

# Run the agent
print("🤖 Vernacular Voice Translator — Speak to Translate!")
while True:
    print("\nSay something or type 'quit' to exit.")
    spoken_text = get_voice_input()
    if spoken_text.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    translated = translate_to_english(spoken_text)
    print("📝 English Translation:", translated)
    speak(translated)

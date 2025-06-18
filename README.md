🗣️ Vernacular to English Voice Translator
This is a simple AI-powered voice agent that listens to a spoken sentence in vernacular (e.g., Swahili) and translates it into English — then speaks the translation back to the user. Great for learning, accessibility, or communication!

🚀 Features
🎤 Voice input using a microphone (speech recognition)

🔤 Vernacular-to-English translation using a keyword dictionary

🔊 English voice output (text-to-speech)

📦 Runs fully offline (no API required)

🛠️ Built With
Python 🐍

speech_recognition for converting speech to text

pyttsx3 for text-to-speech

Custom translation dictionary for local language phrases

📦 Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/vernacular-translator.git
cd vernacular-translator
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Or install manually:

bash
Copy
Edit
pip install speechrecognition pyttsx3
Run the translator:

bash
Copy
Edit
python translator.py
🧠 How It Works
You speak a sentence in your local language (e.g., “habari mimi ni mwanafunzi”).

The program converts your speech to text.

It looks up each word in a dictionary and translates it.

It reads the English translation aloud.

📝 Sample Words/Phrases
Vernacular	English
habari	hello
asante	thank you
mimi ni mwanafunzi	I am a student
nataka maji	I want water

You can add more phrases to the dictionary in the code!

📌 Future Improvements
Add support for full-sentence machine translation (using Hugging Face Transformers)

Add web UI with Gradio or Streamlit

Add support for multiple local languages

🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss what you would like to change.

🧑‍💻 Author
Marylyne Musau – LinkedIn | GitHub

📄 License
This project is open-source and available under the MIT License.


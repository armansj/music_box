MusicBox with Voice Command Control 🎶

This project is a voice-controlled music player that uses Python to listen for commands and interact with your music library. It employs Google's Speech Recognition API for voice input and Google Text-to-Speech (gTTS) to respond verbally. The system can play, stop, and skip music tracks using simple voice commands.

🛠 Features

Play specific music tracks by name.
Play random tracks from your music library.
Stop or skip tracks with voice commands.
Voice interaction with personalized greetings.
Cross-platform compatibility: works on both Windows and macOS (adjusts audio playback methods accordingly).
📦 Requirements

To run the project, you'll need to install the following Python libraries:

bash
Copy code
pip install SpeechRecognition gTTS
🚀 How to Run

Set up your music library:
Place all your .mp3 music files in the ~/Desktop/musicbox directory on macOS, or adjust the music_directory variable in the code for other platforms.
Run the Python script:
The system will start listening for voice commands after greeting you.
Available Voice Commands:
"Melissa, hello" or "Melissa, how are you?" – Initiates a greeting.
"Melissa, play music" – Asks for a specific track to play.
"Melissa, stop music" – Stops the current track.
"Melissa, next music" – Skips to the next track.
"Melissa, play random music" – Plays a random track from the music library.

Melissa: "Hello Arman. How are you?"
User: "Not bad."
Melissa: "What can I do for you?"
User: "Play music."
Melissa: "Which music would you like to play?"
User: "Track one."
Melissa: "Playing track one."


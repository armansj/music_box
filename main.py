import os
import random
import speech_recognition as sr
from gtts import gTTS
import subprocess
import time
import threading

music_directory = os.path.expanduser("~/Desktop/musicbox")

recognizer = sr.Recognizer()

def get_music_files():
    return [f for f in os.listdir(music_directory) if f.endswith('.mp3')]

music_files = get_music_files()
current_track = None
player_process = None
stop_event = threading.Event()

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    if os.name == 'posix':
        subprocess.call(["afplay", "response.mp3"])
    elif os.name == 'nt':
        os.system("start /MIN wmplayer response.mp3")
    time.sleep(2)

def play_music(track_name):
    global current_track, player_process
    file_path = os.path.join(music_directory, track_name + ".mp3")
    if os.path.exists(file_path):

        stop_music()
        if os.name == 'posix':
            player_process = subprocess.Popen(["afplay", file_path])
        elif os.name == 'nt':
            player_process = subprocess.Popen(["start", "/MIN", "wmplayer", file_path], shell=True)
        current_track = track_name
        speak(f"Playing {track_name}.")
    else:
        speak("Sorry, I could not find the track.")

def stop_music():
    global player_process
    if player_process:
        print("Stopping music...")
        try:
            if os.name == 'posix':
                player_process.terminate()
                player_process.wait()
            elif os.name == 'nt':
                os.system(f"taskkill /F /PID {player_process.pid}")
            player_process = None
            speak("Music stopped.")
        except Exception as e:
            print(f"Error stopping music: {e}")

def play_random_music():
    global current_track
    if music_files:
        random_track = random.choice(music_files).replace('.mp3', '')
        play_music(random_track)
        speak(f"Playing random track: {random_track}")
    else:
        speak("No music files found.")

def next_music():
    global current_track
    if current_track:
        try:
            current_index = music_files.index(current_track + '.mp3')
            next_index = (current_index + 1) % len(music_files)
            next_track = music_files[next_index].replace('.mp3', '')
            play_music(next_track)
            speak(f"Playing next track: {next_track}")
        except ValueError:
            play_random_music()
    else:
        play_random_music()

def process_command(command):
    global recognizer
    if "melissa" in command:
        if "hello" in command or "how are you" in command:
            speak("Hello Arman. How are you?")
            time.sleep(5)  # Allow time for response
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                response = recognizer.recognize_google(audio).lower()
                if "not bad" in response:
                    speak("What can I do for you?")
                else:
                    speak("I didn't catch that. Please say 'not bad' if you are doing well.")
        elif "play music" in command:
            speak("Which music would you like to play?")
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                track_name = recognizer.recognize_google(audio).lower()
                play_music(track_name)
        elif "stop music" in command:
            stop_music()
        elif "next music" in command:
            next_music()
        elif "play random music" in command:
            play_random_music()
        else:
            speak("Sorry, I didn't understand the command.")
    else:
        speak("Please address me as Melisa.")

def listen_for_command():
    global recognizer, stop_event
    with sr.Microphone() as source:
        print("Listening for commands...")
        while not stop_event.is_set():
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Command received: {command}")

                threading.Thread(target=process_command, args=(command,)).start()

            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError:
                print("Sorry, there was a problem with the speech recognition service.")

if __name__ == "__main__":
    speak("Hello Arman. How are you?")
    listen_for_command()

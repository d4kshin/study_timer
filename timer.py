import time
import os
import platform
import subprocess
import tkinter as tk
import tkinter.messagebox as messagebox

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def play_sound(sound_file):
    try:
        if platform.system() == "Windows":
            import winsound
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
        elif platform.system() == "Darwin":
            subprocess.call(["afplay", sound_file])
        elif platform.system() == "Linux":
            subprocess.call(["aplay", sound_file]) 
        else:
            print("Sound playback not supported on this operating system.")
    except Exception as e:
        print(f"Error playing sound: {e}")
        print("Make sure the sound file exists in the same folder as the .py filee.")

def show_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Pomodoro Timer", message)
    root.destroy() 

def countdown(t, message, sound_file):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\r{message}: {timer}", end="")
        time.sleep(1)
        t -= 1
    print("\nTime's up!")
    play_sound(sound_file)
    show_popup("Time's up!")

def pomodoro_timer(work_duration=25, break_duration=5, long_break_duration=15, num_sessions=4, sound_file="alarm.wav"):
    clear_screen()
    print("Starting Pomodoro Timer...")
    session_count = 0

    while session_count < num_sessions:
        session_count += 1
        print(f"\nSession {session_count}: Work Time!")
        countdown(work_duration * 60, "Work", sound_file)

        if session_count < num_sessions:
            if session_count % 4 == 0:
                print("\nLong Break Time!")
                countdown(long_break_duration * 60, "Long Break", sound_file)
            else:
                print("\nBreak Time!")
                countdown(break_duration * 60, "Break", sound_file)

    print("\nTimer completed!")

if __name__ == "__main__":
    try:
        work_time = int(input("Enter work duration (25 minutes is the default): ") or 25)
        break_time = int(input("Enter short break duration (5 minutes is the defualt): ") or 5)
        long_break_time = int(input("Enter long break duration (15 minutes is the defalut): ") or 15)
        number_of_sessions = int(input("Enter number of work sessions (default is 4): ") or 4)
        sound_path = input("Enter path to sound file (Put it in the root of this folder. Leave as is and press enter if you dont want a custom sound. WAV ONLY!): ") or "alarm.wav"

        pomodoro_timer(work_time, break_time, long_break_time, number_of_sessions, sound_path)

    except ValueError:
        print("Invalid input. PLease check the numbers.")
    except KeyboardPress:
        print("\nTimer interrupted.")

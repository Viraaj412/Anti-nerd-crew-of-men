import football 
import geograpy
import music
from football import start_quiz as football_quiz
from geograpy import start_quiz as geograpy_quiz
from music import start_quiz as music_quiz
def start_quiz():
    score = 0

    print("Welcome to the Anti-Nerd Crew of Men Quizzes!")
    print("Which quiz would you like to take?")
    print("1. football")
    print("2. geography")
    print("3. music")

    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        football.start_quiz() 
    elif choice == "2":
        geograpy.start_quiz() 
    elif choice == "3":
        music.start_quiz() 
    else:
        print("Invalid choice. Please try again.")

start_quiz()

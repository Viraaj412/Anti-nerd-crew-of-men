import football
import geography
import music

def main():
    print("Welcome to the Anti-Nerd Crew of Men Quizzes!")
    print("Which quiz would you like to take?")
    print("1. Football")
    print("2. Geography")
    print("3. Music")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        football.start_quiz()
    elif choice == "2":
        geography.start_quiz()
    elif choice == "3":
        music.start_quiz()
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

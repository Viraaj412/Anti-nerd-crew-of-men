def start_quiz():
    score = 0  # Initialize score variable

    # Question 1
    print("Welcome to the Music Quiz!")
    print("Who is known as the King of Pop?")
    print("A. Elvis Presley")
    print("B. Michael Jackson")
    print("C. Freddie Mercury")
    print("D. Prince")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "B":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is B. Michael Jackson.")
    print(f"Your current score: {score}\n")

    # Question 2
    print("Which musical instrument has 88 keys?")
    print("A. Guitar")
    print("B. Violin")
    print("C. Piano")
    print("D. Flute")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "C":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is C. Piano.")
    print(f"Your current score: {score}\n")

def start_quiz():
    score = 0  # Initialize score variable

    # Question 1
    print("Welcome to the Football Quiz!")
    print("Who won the 2018 FIFA World Cup?")
    print("A. Brazil")
    print("B. Spain")
    print("C. Germany")
    print("D. France")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "D":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is D. France.")
    print(f"Your current score: {score}\n")

    # Question 2
    print("Which player has won the most Ballon d'Or awards?")
    print("A. Lionel Messi")
    print("B. Cristiano Ronaldo")
    print("C. Zinedine Zidane")
    print("D. Ronaldinho")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "A":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is A. Lionel Messi.")
    print(f"Your current score: {score}\n")

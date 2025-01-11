def start_quiz():
    score = 0  # Initialize score variable

    # Question 1
    print("Welcome to the Geography Quiz!")
    print("What is the capital of France?")
    print("A. Paris")
    print("B. Berlin")
    print("C. Madrid")
    print("D. Rome")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "A":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is A. Paris.")
    print(f"Your current score: {score}\n")

    # Question 2
    print("Which is the largest continent?")
    print("A. Africa")
    print("B. Europe")
    print("C. Asia")
    print("D. Antarctica")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "C":
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is C. Asia.")
    print(f"Your current score: {score}\n")

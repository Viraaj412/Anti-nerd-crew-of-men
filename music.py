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

    print("Question 3: Who is known as the queen of rap?")
    print("A. Cardi B")
    print("B. Megan Thee stalion")
    print("C. Nicki Minaj")
    print("D. Doja cat")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "C":  # Replace "" with the correct answer choice
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is C. nicki minaj.")
    print(f"Your current score: {score}\n")

    print("Which rapper released the song known as the the Box")
    print("A. Roddy Rich")
    print("B. Lil baby")
    print("C. Juice wrld")
    print("D. Pop smoke")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "A":  # Replace "" with the correct answer choice
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is A. Roddy Rich.")
    print(f"Your current score: {score}\n")

    print("Question 4: Which artist is known for their alter ego Slim Shady")
    print("A.  Drake")
    print("B. Eminem")
    print("C. Jay Z")
    print("D. J.cole")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "B":  # Replace "" with the correct answer choice
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is B. Eminem.")
    print(f"Your current score: {score}\n")

 
    print("Question 5: [Your question here]")
    print("A. ")
    print("B. ")
    print("C. ")
    print("D. ")
    
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == "":  # Replace "" with the correct answer choice
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is A. [Correct Answer].")
    print(f"Your current score: {score}\n")


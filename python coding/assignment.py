import random

# All 10 questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Picasso", "B. Da Vinci", "C. Michelangelo", "D. Van Gogh"],
        "answer": "B"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"],
        "answer": "C"
    },
    {
        "question": "Which language is used to write web pages?",
        "options": ["A. HTML", "B. C++", "C. Python", "D. Java"],
        "answer": "A"
    },
    {
        "question": "Which instrument has keys, pedals, and strings?",
        "options": ["A. Violin", "B. Guitar", "C. Piano", "D. Drums"],
        "answer": "C"
    },
    {
        "question": "What is H2O commonly known as?",
        "options": ["A. Salt", "B. Oxygen", "C. Water", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["A. Amazon", "B. Nile", "C. Ganga", "D. Yangtze"],
        "answer": "B"
    },
    {
        "question": "Who discovered gravity?",
        "options": ["A. Galileo", "B. Edison", "C. Newton", "D. Tesla"],
        "answer": "C"
    }
]

# Game loop
while True:
    score = 0

    # Ask how many questions
    try:
        total_qs = int(input("How many questions do you want? (1 to 10): "))
    except ValueError:
        print("❗ Please enter a valid number.")
        continue

    if total_qs < 1 or total_qs > 10:
        print("❗ Please enter a number between 1 and 10.")
        continue

    # Randomly pick questions
    selected = random.sample(questions, total_qs)

    # Ask each question
    for q in selected:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        while True:
            ans = input("Your answer (A/B/C/D): ").upper()
            if ans in ["A", "B", "C", "D"]:
                break
            else:
                print("❌ Invalid choice. Please enter only A, B, C, or D.")

        if ans == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was {q['answer']}")

    # Final score
    print(f"\nYour score: {score}/{total_qs}")

    # Play again?
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing!")
        break
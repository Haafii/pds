
import random
score = 0
questions =[
    {
        "question" : " what is the color of crow ? ",
        "options" : ["A.white", "B.Black", "C.Brown", "D.Red" ],
        "answer" : "B"
    },
    {
        "question" : " what is the color of Milk ? ",
        "options" : ["A.white", "B.Black", "C.Brown", "D.Red" ],
        "answer" : "A"
    },
    {
        "question" : " Captial of India ? ",
        "options" : ["A.Delhi", "B.Kerala", "C.Tamil Nadu", "D.Goa" ],
        "answer" : "A"
    },
    {
        "question" : " what is the mother toungue of kerala ? ",
        "options" : ["A.Hindi", "B.Arabi", "C.Tamil", "D.Malayalam" ],
        "answer" : "D"
    },
    {
        "question" : " what is the square root of 9 ? ",
        "options" : ["A.4", "B.3", "C.5", "D.9" ],
        "answer" : "B"
    },
]

while True:
    totalquestions = int(input("enter the number of questions you want upto 5: "))
    if(totalquestions >= 5):
        print("invalid")
        continue
    
    selectquestion = random.sample(questions,totalquestions)

    for q in selectquestion:
        print("\n" + q["question"]) 
        for option in q["options"]:
           print(option)
        
        while True:
            ans = input("Your answer (A/B/C/D): ").upper()
            if ans in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid")

        if ans == q["answer"]:
            print("Correct")
            score += 1
        else:
            print("Wrong! Correct answer was", q["answer"])

    
    print("\nYour score: ", score)


    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
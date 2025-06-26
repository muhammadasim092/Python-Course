
# Kaun Banega Crorepati - Pakistan Version

# questions = {
#     "question" : "What is the capital of Pakistan?",
#     "options" : ["A. Lahore", "B. Islamabad", "C. Karachi", "D. Peshawar"],
#     "answer" : "B"
# },
# {
#     "question": "Who is the Prime Minister of Pakistan in 2022?",
#     "options":  ["A. Imran Khan", "B. Shahbaz Sharif", "C. NawazShreef"],
#     "answer": "B"
#     },
# {

    
#     "question": "What is the largest city in Pakistan?",
#     "options": ["A. Lahore", "B. Karachi", "C. Faisalabad"],
#     "answer": "B"
#     },
# {
#     "question": "What is the official language of Pakistan?",
#     "options": ["A. English", "B. Urdu", "C. Punjabi"],
#     "answer": "B"
#     },
# {
#     "question": "Who is the founder of Pakistan?",
#     "options": ["A. Muhammad Ali Jinnah", "B. Quaid-e-Azam"],
#     "answer": "A"
# },
# {
#     "question": "What is the currency of Pakistan?",
#     "options": ["A. Pakistani Rupee", "B. US Dollar"],
#     "answer": "A"
# }

# prize_per_question = 1000
# total_prize = 0 

# print("Wellcome to kon bnaga cror pati Pakistan Version")

# for i, q in enumerate(questions):
#     print(f"Question {i+1}: {q['question']}")
#     for option in q['options']:
#         print(f"{option}")

# user_answer = input("Enter your answer (A/B/C/D): ")
# if user_answer == q['answer']:
#     total_prize += prize_per_question
#     print( f"Correct answer. You have earne, {prize_per_question} PKR")

# else:
#     print(f"Incorrect answer. The correct answer is {q['answer']}")
#     print("Game over")
#     # break
# print( f"Your total prize you are takeing to home  is {total_prize} PKR")


questions = [
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
["Which language was used to create the facebook ?" , "Python" , "French" , "php", "JavaScript",3],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
i = 0 
for i in range (0 ,  len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    reply = int(input("Enter your Answer (1-4): "))
    if reply == question[-1]:
        print(f"Correct answer , You have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
    else:
        print(f"Incorrect answer , You have lost Rs. {levels[i]}")
        break
    print("You are takeing money with you is {money}")

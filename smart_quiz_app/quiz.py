#Step 1 import modules/Libraries
import random #generate random numbers or shuffle items
import json  #load or save data in .json format
#Fore → setting text color (like red, green, cyan, etc.), Style → styling text (like making it bold or dim).
#init() → initializes colorama so colors work correctly on Windows/macOS/Linux terminals
from colorama import Fore, Style, init  
init(autoreset=True) #Means after each print, the color will automatically reset to normal text color

#Step 2: Welcome message 
print(Fore.CYAN + Style.BRIGHT + "Welcome to the Smart Quiz App!")

#Step 3 questions - a list of dictionaries ([ {...}, {...}, {...} ])
questions = [
    {
        "question":"Which language is this program written in?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": "Python"
    },
    {
        "question":"What is the capital of France?",
        "options":["Berlin", "Madrid", "Paris", "Rome"],
        "answer":"Paris"
    },
    {
        "question":"What is 2+2?",
        "options":["3", "4", "5", "6"],
        "answer":"4"
    },
]

#Step 4 :  Randomly rearranges the elements of a list in place and initialize score 
random.shuffle(questions)
score = 0

#Step 5 : Loop through each dictionary (question) inside the list questions
for q in questions:
    print(f"\n{q['question']}") #gets the text from the "question" key in the dictionary
    for idx, option in enumerate(q['options'], start=1): #start=1 which means 1-4 for options not start=0 which means 0-3
        print(f"{idx}. {option}") #f before string means f-string → allows you to insert variables inside {}
    try:
        choice = int(input(Fore.YELLOW+"Your answer (1-4): "))
        if q['options'][choice-1] == q['answer']: #Because Python list indices start at 0, we subtract 1
            print(Fore.GREEN + "Correct!")
            score += 1
        else:
            print(Fore.RED + f"Wrong! The correct answer is : {q['answer']}")
    except (ValueError, IndexError):
        print(Fore.RED + "Invalid input! Please enter a number between 1 and 4.")
    
print(Fore.CYAN + Style.BRIGHT + f"\nQuiz Over! Your final score is: {score}/{len(questions)}")

#Step 6 : Final evaluation based on score 
if score == len(questions): #all answers correct
    print(Fore.GREEN + Style.BRIGHT + "Excellent! Your got a perfect score!")
elif score >= len(questions)//2: #score is at least half of total
    print(Fore.YELLOW + "Good job! You did well.")
else: 
    print(Fore.RED + "Better luck next time!")
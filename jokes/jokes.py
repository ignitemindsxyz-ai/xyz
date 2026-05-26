import json
import random

user_name = input("What is your username?: ")

print(f"Hello {user_name}")
know = input("What would you like to know?: ").lower().strip()

def joke():
    with open("jokes.txt", "r", encoding="utf-8") as file:
        jokes = file.read()
        jokes_list = jokes.strip().split("\n\n")
        jokes = []
        for joke in jokes_list:
            jokes.append(joke.strip())
            return random.choice(jokes)

def answer():
    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            return json.load(file)
        
    except FileNotFoundError:
        print("The file questions.json was not found.")
        return {}

def answer_question(question):
    temporary_answer = answer()
    question = answer()
    question = question.lower()
    for q in answer:
        if q.lower() in question:
            return answer[q]
        return "Sorry, I don't have an answer for that question."

if know == "joke":
    jokes = joke()
    random_joke = random.choice(jokes)
    print(random_joke)

else:
    print(answer_question(know))
    response = answer_question(know)
    print(response)

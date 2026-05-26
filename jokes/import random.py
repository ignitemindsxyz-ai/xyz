import random
import json

def clean_text(text):
    text = text.lower()
    punctuation = "?"
    for p in punctuation:
        text = text.replace(p, "")
    return text

def load_answer():
    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            return json.load(file)
        
    except FileNotFoundError:
        print("The file questions.json was not found.")
        return {}

def load_question(user_question):
    user_input = user_question.lower().strip()
    answer = load_answer()
    if "joke" in user_input:
        jokes = load_jokes()
        return random.choice(jokes)
    for q in answer:
        if q.lower() in user_input:
            return answer[q]
        fallback = [
            "Sorry, I don't have an answer for that question.",
            "I'm not sure how to answer that.",
            "That's an interesting question, but I don't have an answer for it."
        ]
    return random.choice(fallback)

def load_jokes():
    try:
         with open("jokes.txt", "r", encoding = "utf-8") as file:
            jokes = file.read()
            jokes_list = jokes.strip().split("\n\n")
            return [j.strip() for j in jokes_list if j.strip()]
        
    except FileNotFoundError:
       print("The file jokes.txt was not found.")
       return []

print("Chat started. Type 'exit' to quit.")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Goodbye!")
        break

    response = load_question(user)
    print("Bot:", response)
import random
import json

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
    for q in answer:
        if q.lower() in user_input:
            return answer[q]
        fallback = [
            "Sorry, I don't have an answer for that question.",
            "I'm not sure how to answer that.",
            "That's an interesting question, but I don't have an answer for it."
        ]
    return random.choice(fallback)

print("Chat started. Type 'exit' to quit.")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Goodbye!")
        break

    response = load_question(user)
    print("Bot:", response)
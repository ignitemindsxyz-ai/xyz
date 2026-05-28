def add_user_name():
    user_name = []
    
def conversation():
    user_name = input("What is your name? : ")
    if not user_name :
        print("Name can not be empty.")

    print(f"Hello {user_name}. How are you?")
    mood = input("").lower().strip()
    if mood == "i am fine":
        print("That is good to hear.")

    elif mood == "i am not fine":
        print("What happened? And could i help you with something?")
        mood_answer = input("").lower().strip()

        if mood_answer == "no":
            print("Sorry to hear that, I hope it gets better soon")

        elif mood_answer == "yes":
            print("Great, how can I help you?")        

add_user_name()
conversation()
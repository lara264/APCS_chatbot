import random

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y", "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False

def has_keyword(statement, keywords):
    statement = " " + statement
    for word in keywords:
        word = " " + word
        if word in statement:
            return True
    return False

def start():
    pass

def get_random():
    response = ["Cool", "That's interesting", "Tell me more", "Really?", "Are you sure?"]
    return random.choice(response)

def get_response(statement):
    statement = statement.lower()

    positive = ["like", "happy", "excited", "positive", "love"]
    negative = ["sad", "unhappy", "upset", "negative", "hate"]

    if has_keyword(statement, positive):
        response = "Tell me more"
    elif has_keyword(statement, ["sense"]):
        response = "It makes sense to me"
    elif has_keyword(statement, ["you"]):
        response = "What about me?"
    elif has_keyword(statement, negative):
        response = "I'm sorry you feel that way"
    else:
        response = get_random()

    return response

def play():
    talking = True

    print("Hello :) I'm Awkward")
    print("What's your name?")
    name = input()
    print("Nice to meet you " + name)
    print("Tell me about yourself")

    response = ""

    while talking:
        statement = input(name + ":")
        array = statement.split(":")
        statement = array[0]
        statement = statement.lower()

        if (statement in ["goodbye", "bye"]):
            talking = False
        elif statement == "what":
            response = response.lower()
            print("Awkward: I said " + response)
        elif statement == "why":
            response = "Why not?"
            print("Awkward: " +  response)
        else:
            response = get_response(statement)
            print("Awkward: " +  response)

def end():
    print("Goodbye :)")

start()

playing = True
while(playing):
    play()
    playing = confirm("Would you like to chat again?")

end()
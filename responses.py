import random


def get_response(message: str) -> str:

    p_message = message.lower()

    rock_paper_scissors = ["rock", "paper", "scissors"]

    if p_message == "hello":
        return "Hey there!"

    if p_message == "roll":
        return str(random.randint(1, 6))
 
    if p_message in rock_paper_scissors:
        return str(random.choice(rock_paper_scissors).title())

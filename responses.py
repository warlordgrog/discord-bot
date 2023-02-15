import random



def get_response(message: str) -> str:
    p_message = message.lower()
    a = ['Rock', 'Paper', 'Scissors']
    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))
 
    if message == 'Rock':
        return str(random.choice(a))

    if message == 'Paper':
        return str(random.choice(a))

    if message == 'Scissors':
        return str(random.choice(a))






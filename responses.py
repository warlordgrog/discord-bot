import random



def get_response(message: str) -> str:
    p_message = message.lower()
    a = ['Rock', 'Paper', 'Scissors']
    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message.startswith('gejus'):
        return 'taip'

    if p_message.endswith('gejus'):
        return 'taip'

    if p_message.startswith('nig'):
        return '🤨'

    if p_message.endswith('nig'):
        return '🤨'

    if p_message.startswith('neg'):
        return '🤨'

    if p_message.endswith('neg'):
        return '🤨'

    if message == 'Rock':
        return str(random.choice(a))

    if message == 'Paper':
        return str(random.choice(a))

    if message == 'Scissors':
        return str(random.choice(a))

    if p_message == 'dj khaled':
        return 'https://tenor.com/view/dj-khaled-another-one-gif-24892740'

    if p_message == 'cigonas':
        return 'https://open.spotify.com/artist/7EJlB4S1doJPfMLfDGSp3P?si=ORFgZhEBQXqRXRutvDapQg'





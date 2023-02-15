import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'OTk0MjUzNDIxNTM4NDU5NzA4.GAwlW5.R5eIXBzIh1nhrrgB4gJ6rNwMBPKnnlMfmlAYNI'
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    client = discord.Client(intents=intents)





    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.author.id == 0000000000000 and message.startswith("https"):
            await message.delete()
            # can return here as we deleted message - no need to process anything else
            return

        username = message.author.name
        user_message = message.content
        channel = message.channel.name
        print(f'{username} said: "{user_message}" ({channel})')
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run('OTk0MjUzNDIxNTM4NDU5NzA4.GAwlW5.R5eIXBzIh1nhrrgB4gJ6rNwMBPKnnlMfmlAYNI')

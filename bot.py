import discord
import responses

# user id of the user we want to delete links for
MY_ID = 189458414764687360

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if not response:
            # response is empty - return
            return

        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = ""
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # need to use `message.content` here as that's the actual message content
        if message.author.id == MY_ID and message.content.startswith("https"):
            await message.delete()
            # can return here as we deleted message - no need to process anything else
            return

        username = message.author.name
        user_message = message.content
        channel = message.channel.name
        print(f"{username} said: {user_message} ({channel})")
        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

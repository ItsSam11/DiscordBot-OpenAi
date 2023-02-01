import discord
import responses


async def mensajes_enviados(message, user_message, is_private):
    try:
        response = responses.mensaje_oai(user_message)        

        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

def discord_run_bot():
    TOKEN = '****'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def ready():
        print(f'{client.user} está encendido!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" at the channel: ({channel})')

        if user_message[:2] == '-?':                                
            await mensajes_enviados(message, user_message, is_private=True)
        else:
            await mensajes_enviados(message, user_message, is_private=False)

    client.run(TOKEN)

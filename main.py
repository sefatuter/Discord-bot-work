from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# STEP 0: LOAD TOKEN
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Command prefix
COMMAND_PREFIX = '!'

# STEP 2: COMMAND HANDLING

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty or intents were not activated)')
        return
    
    is_private = user_message[0] == '?'
    
    if is_private: # private messaging functionality
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as err:
        print(err)

# STEP 3: HANDLING THE STARTUP FOR BOT

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# STEP 4: HANDLING INCOMING MESSAGES

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
           
    print(f'[{channel}] {username}: "{user_message}"')
    
    # Check if the message starts with the command prefix
    if user_message.startswith(COMMAND_PREFIX):
        command = user_message[len(COMMAND_PREFIX):]
        await send_message(message, command)

# STEP 5: MAIN ENTRY POINT

def main() -> None:
    client.run(TOKEN)
    
if __name__ == '__main__':
    main()
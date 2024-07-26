from random import choice, randint
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import requests

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return "Well, you're awfully silent..."
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: **{randint(1, 6)}**'
    elif 'flip coin' in lowered:
        return f'You flipped: **{choice(["heads", "tails"])}**'
    elif 'joke' in lowered:
        return choice([
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts."
        ])
    elif 'advice' in lowered:
        return choice([
            "Believe in yourself and all that you are.",
            "Every moment is a fresh beginning.",
            "Don't watch the clock; do what it does. Keep going."
        ])
    else:
        return choice(['I do not understand', 'What are you talking about?', 'Do you mind rephrasing that?'])
    

def get_quote() -> str:
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return f'"{data["content"]}"\n- {data["author"]}'
    else:
        return "Couldn't fetch a quote at the moment. Try again later."
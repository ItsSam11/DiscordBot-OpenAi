import openai
import random

def mensaje_oai(message: str) -> str:
    oai_message = message.lower()

    if message == 'roll':
        return str(random.randint(1,10))

    if oai_message == '!help':
        return '`Para hablar con el modelo de OpenAI, escribe de primero "-" al inicio de cada mensaje.`'

    if oai_message[0] == '-':
        text = oai_message
        # Load your API key from an environment variable or secret management service
        openai.api_key = '****'
    
        response = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0.7, max_tokens=4000)
        
        return response.choices[0].text

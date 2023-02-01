import openai

def mensaje_oai(message: str) -> str:
    oai_message = message.lower()
  
    openai.api_key = '****'

    if oai_message == '!help':
        return '`Escribe "-Hola" para obtener más información.`'

    if oai_message.startswith('-hola'):
        return '''`Hola, soy Chatbot, un proyecto creado por Sam11 y WinstonTheBot, utilizo los recursos de OpenAI para ser más interactivo y estoy alojado en Amazon Web Services.`
        \n`Si quieres usar las funciones de OpenAI tienes que iniciar cada mensaje con un "-" seguido de lo que quieres preguntar o decir.`
        \n`Si quieres recibir mensajes privados de ChatBot tienes que iniciar con un "-?" seguido de lo que quieras preguntar o decir.`
               '''

    if message.lower().startswith('-?hola'):
        return '''`Hola, soy Chatbot, un proyecto creado por Sam11 y WinstonTheBot, utilizo los recursos de OpenAI para ser más interactivo y estoy alojado en Amazon Web Services.`
        \n`Si quieres usar las funciones de OpenAI tienes que iniciar cada mensaje con un "-" seguido de lo que quieres preguntar o decir.`
        \n`Si quieres recibir mensajes privados de ChatBot tienes que iniciar con un "-?" seguido de lo que quieras preguntar o decir.`
               '''
    
    if message.startswith('-?'):
        text = message
            
        response = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0.7, max_tokens=4000)
        
        return response.choices[0].text

    if oai_message[0] == '-':
        text = oai_message
        
        response = openai.Completion.create(model="text-davinci-003", prompt=text, temperature=0.7, max_tokens=4000)
        
        return response.choices[0].text

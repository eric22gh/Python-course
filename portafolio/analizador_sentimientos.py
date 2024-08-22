# vamos a crear un analizador de sentimientos, sencillo
from textblob import TextBlob # biblioteca de analisis de sentimiento en ingles
class AnalizadorDeSentimiento:
    def analizar(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return 'Positivo'
        elif analisis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negativo'
        
analizar = AnalizadorDeSentimiento()
texto = 'Im fellings sooo sad'
print(analizar.analizar(texto))

#### ahora vamos a crear un analizador de sentimiento mas avanzado
import openai  as IA 
IA.api_key = "https://api.openai.com/v1" # hay que pagar para utilizarla, esta es solo un ejemplo
system_init =  ''' Tu nombre es el Analizador de Sentimiento. Tu trabajo es analizar texto y dar un resumen de lo que se le dijo. 
Responde en un resumen de 4 palabras. Responde de la siguiente forma: -1 es negativo, 0 es neutral, 1 es positivo, 2 es muy positivo, 3 es muy negativo.

'''
mensaje = [{"role": "system", "content": system_init}]
class AnalizadorDeSentimiento:
    def analizar(self, polaridad):
        if polaridad > -0.8 and polaridad <= 0.3:
            return "\x1b[1,31m" + "Negativo" + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad < 0.1:
            return "\x1b[1,31m" + "algo negativo" + "\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1,32m" + "Neutral" + "\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1,32m" + "algo positivo" + "\x1b[0;37m"
        elif polaridad > 0.4 and polaridad <= 0.6:
            return "\x1b[1,32m" + "Positivo" + "\x1b[0;37m"
        elif polaridad > 0.6 and polaridad <= 1:
            return "\x1b[1,33m" + "Muy positivo" + "\x1b[0;37m"
        elif polaridad > 1 and polaridad <= 1.5:
            return "\x1b[1,34m" + "demasiante positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1,36m" + "Muy negativo" + "\x1b[0;37m"
        
analizando = AnalizadorDeSentimiento()
while True:
    texto = input("\x1b[1,33m" + "Dime algo: " + "\x1b[0;37m")
    mensaje.append({"role": "user", "content": texto})
    response = IA.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensaje,
        max_tokens=8
    )
    
    respuesta = response.choices[0].message["content"]
    mensaje.append({"role": "assistant", "content": respuesta})
    sentimiento = analizando.analizar(float(respuesta))
    print(sentimiento)



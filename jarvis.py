import speech_recognition as sr
import pyttsx3
from decouple import config

OPENAPI_KEY = config("OPENAPI_KEY", cast=str)

from openai import OpenAI

client = OpenAI(api_key=OPENAPI_KEY)


def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


r = sr.Recognizer()


def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("JARVIS: Im listening")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                print(f'you speak: {MyText}')

                return MyText
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")

def chatGPT(message):
    chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=message, stop=None)
    return chat_completion.choices[0].message.content

while True:
    text = record_text()
    res = chatGPT([{"role": "user", "content": text}])
    print(f"JARVIS: {res}")
    speak_text(res)
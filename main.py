from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def listen_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: "+ our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"

    # return input("Скажите вашу команду: ")

def do_this_command(message):
    message = message.lower()
    print(message)
    if "привет" in message:
        say_message("Привет друг!")
    elif "пока" in message:
        say_message("Пока!")
        exit()
    else:
        say_message("Команда не распознана")

def say_message(message):
    voice = gTTS(message, lang='ru')
    file_voice_name = "_audio_"+str(time.time())+" "+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("голосовой ассистент:"+message)

if __name__ == '__main__':
    while True:
        command = listen_command()
        print(command)
        do_this_command(command)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

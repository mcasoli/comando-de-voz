# PROJETO JOANA VOICE v0.1
#--------------------------------------------------------------


"""IMPORTAÇÕES"""
import keyboard, threading 

import os, time, sys
import pyautogui as py
import speech_recognition as sr #pip install SpeechRecognition
import pyttsx3 #pip install pyttsx3
#import pyaudio #pip install pyaudio
#print (sr.Microphone().list_microphone_names())

from selenium import webdriver #importa o webdriver usando o módulo Selenium <<Selenium necessita ser instalado via terminal = 'pip install selenium'>>
from webdriver_manager.chrome import ChromeDriverManager #<<necessita ser instalado via terminal = 'pip install webdriver-manager'>>
from selenium.webdriver.chrome.service import Service


rec_mic = sr.Recognizer()

"""Propriedades Voz.Bot"""
voice = pyttsx3
voz_bot = pyttsx3.init()

veloc = voz_bot.getProperty('rate')
voz_bot.setProperty('rate', veloc-0) #+50
'''--------------------------------------'''
about_text = pyttsx3.speak("Olá, eu sou a Joana. O primeiro comando de voz usado pelo Grupo Doomini para ações de automação.")
time.sleep(1)

say_ = pyttsx3.speak("Diga: Olá, Joana, e aguarde...")

test = True
while test:
        with sr.Microphone(1) as mic:
                rec_mic.adjust_for_ambient_noise(mic)
                audio = rec_mic.listen(mic)
                texto = "None"
                try:
                        texto = rec_mic.recognize_google(audio, language= "pt-BR")
                        print (texto)
                except:
                      pass
                       
        if texto == "Olá Joana":
                #test = False
                texto = ""
                with sr.Microphone(1) as mic:
                        rec_mic.adjust_for_ambient_noise(mic)
                        print ("Joana na escuta...")
                        voz_bot.say("Joana na escuta.")
                        voz_bot.runAndWait()

                        audio = rec_mic.listen(mic)
                        try:
                                texto = rec_mic.recognize_google(audio, language= "pt-BR")
                                print (texto)
                                voz_bot.say("Ok")
                                voz_bot.runAndWait()
                        except:
                                print ("Não compreendi sua fala, tente novamente.")
                                voice.speak("Não compreendi sua fala, tente novamente.") 
                                test = True
        print ("Buscando fala...")

        mensagem = texto.split()

        # Acessar Internet
        list_nav = ["acessar", "acesse", "navegue", "navegar", "site", "internet"]
        for item in mensagem:
                if item in list_nav:
                        voz_bot.say("Entendi que você deseja acessar um site na internet")
                        voz_bot.runAndWait()
                        
                        with sr.Microphone(1) as mic:
                                        rec_mic.adjust_for_ambient_noise(mic)
                                        print ("Fale agora o endereço")
                                        voz_bot.say("Fale agora o endereço:")
                                        voz_bot.runAndWait()

                                        audio = rec_mic.listen(mic)
                                        try:
                                                url = rec_mic.recognize_google(audio, language= "pt-BR")
                                                print (url)

                                                url = str(url).replace(" ","")
                                                
                                                voz_bot.say("Acessando...")
                                                voz_bot.runAndWait()

                                                nav = webdriver.Chrome(service= Service(ChromeDriverManager().install())) 
                                                nav.get(f"http://www.{url}")
                                                pass

                                                
                                        except:
                                                print ("Não compreendi sua fala, tente novamente.")
                                                voice.speak("Não compreendi sua fala, tente novamente.") 
                                                test = True
                                                nav.quit()
                        break
                

        # Digitar no texto no Word
        list_nav = ["Word", "digite", "texto"]
        for item in mensagem:
                if item in list_nav:
                        voz_bot.say("Entendi que você deseja um texto no Microsoft Word.")
                        voz_bot.runAndWait()
                
                        os.startfile(r'C:\Program Files\Microsoft Office\Office16\winword.exe')
                        voice.speak("Um momento...")
                        time.sleep(3)
                        py.press("enter")

                        with sr.Microphone(1) as mic:
                                rec_mic.adjust_for_ambient_noise(mic)
                                print ("Fale agora o texto desejado")
                                voz_bot.say("Fale agora o texto desejado:")
                                voz_bot.runAndWait()

                                audio = rec_mic.listen(mic)
                                try:
                                        frase = rec_mic.recognize_google(audio, language= "pt-BR")
                                        print (frase)
                                        voz_bot.say("Ok")
                                        voz_bot.runAndWait()

                                        py.write (frase)
                                        voice.speak(f"Você disse: {frase}") 
                                        test = True
                                        pass

                                        
                                except:
                                        print ("Não compreendi sua fala, tente novamente.")
                                        voice.speak("Não compreendi sua fala, tente novamente.") 
                                        test = True
                        break       
        
        
        # Tchau, Joana
        if mensagem == "tchau":
               pyttsx3.speak("Até mais!")
               sys.exit()
        





















"""

voz_bot.say("Era uma vez... um pai chamado Seu Dacir. \n"
        "Esse pai teve um pequeno filho e precisou dar um nome para ele.\n"
        "Ele resolveu homenagear os Alevinos, que são pequenos filhotinhos de peixe. Alevinos. \n"
        "E resolveu chamar seu filho de Alev. Seu Dacir registrou no cartório. \n"
        "Mas for um froblema em fua fala, feu filho foi refristado com o nome Alef Dacir, o Alef. \n"
        "Logo em seguida, seu Dacir fugiu. Fim.")
voz_bot.runAndWait()

"""
import os
import subprocess
import psutil
import webbrowser
import pyautogui

from langs.ru.voice import *
from langs.en.voice import *
from langs.en.listen import *






#sites
def open_search(text_ru, text_en):
    webbrowser.open('https://yandex.com/')

def open_ege(text_ru, text_en):
    webbrowser.open('https://ege.sdamgia.ru/')

def open_sdam(text_ru, text_en):
    webbrowser.open('https://sdamgia.ru/')

def open_mesh(text_ru, text_en):
    webbrowser.open('https://dnevnik.mos.ru/diary/schedules/schedule')

def open_youtube(text_ru, text_en):
    webbrowser.open('https://www.youtube.com/')

def open_translator(text_ru, text_en):
    webbrowser.open('https://translate.yandex.ru/')


#apps
def open_discord(text_ru, text_en):
    try:
        subprocess.Popen(['D:/My Projects/programming/expo v-2/apps/Discord.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak_ru('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_discord(text_ru, text_en):
    process_name = 'Discord.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
        speak_ru('Указанный процесс не найден.')
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")
        speak_ru('Указанный процесс не существует.')



def open_browser(text_ru, text_en):
    try:
        subprocess.Popen(['D:/My Projects/programming/expo v-2/apps/Yandex.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak_ru('Указанный процесс не найден.')('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")
#ФИКСИТЬ ЗАКРЫТИЕ
def close_browser(text_ru, text_en):
    process_name = 'browser.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
        speak_ru('Указанный процесс не найден.')
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")
        speak_ru('Указанный процесс не существует.')



def open_valorant(text_ru, text_en):
    try:
        subprocess.Popen(['D:/My Projects/programming/expo v-2/apps/VALORANT.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak_ru('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_valorant(text_ru, text_en):
    process_name = 'VALORANT.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
        speak_ru('Указанный процесс не найден.')
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")
        speak_ru('Указанный процесс не существует.')



def open_minecraft(text_ru, text_en):
    try:
        subprocess.Popen(['D:/My Projects/programming/expo v-2/apps/Minecraft.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak_ru('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_minecraft(text_ru, text_en):
    process_name = 'TLauncher.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
        speak_ru('Указанный процесс не найден.')
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")
        speak_ru('Указанный процесс не существует.')



def open_steam(text_ru, text_en):
    try:
        subprocess.Popen(['D:/My Projects/programming/expo v-2/apps/Steam.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak_ru('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_steam(text_ru, text_en):
    process_name = 'steam.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
        speak_ru('Указанный процесс не найден.')
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")
        speak_ru('Указанный процесс не существует.')



def open_telegram(text_ru, text_en):
    try:
        subprocess.Popen(['D:/My Projects/programming/expo v-2/apps/Telegram.lnk'], shell=True, close_fds=True)
    except Exception as e:
        speak_ru('не могу найти такую программу. ознакомьтесь с инструкцией.')
        print(f"Произошла ошибка при запуске ярлыка: {e}")

def close_telegram(text_ru, text_en):
    process_name = 'Telegram Desktop.exe'
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == process_name:
                process.terminate()
                print(f"Процесс {process_name} успешно завершен.")
                return
        print(f"Процесс {process_name} не найден.")
        speak_ru('Указанный процесс не найден.')
    except psutil.NoSuchProcess:
        print(f"Процесс {process_name} не существует.")
        speak_ru('Указанный процесс не существует.')




def open_apps(text_ru, text_en):
    text_en = listen_en()
    speak_ru('Команда в разработке.')

    apps_list = []

    for app in apps_list:
        if app in text_en:
            try:
                subprocess.Popen([f'D:/My Projects/programming/expo v-2/apps/{app}.lnk'], shell=True, close_fds=True)
            except Exception as e:
                speak_ru('Указанный процесс не найден.')('не могу найти такую программу. ознакомьтесь с инструкцией.')
                print(f"Произошла ошибка при запуске ярлыка: {e}")
            break
        else:
            speak_ru('Я не могу найти ваше приложение. Пожалуйста, ознакомьтесь с инструкцией пользования.')
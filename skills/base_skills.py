import os, webbrowser, sys, requests, subprocess, psutil, pyautogui
import config, words
from num2words import num2words
from langs.ru.voice import *
from langs.en.voice import *
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
from ru_word2number import w2n
from deep_translator import GoogleTranslator




def full_weather(text_ru, text_en):
    city = config.CITY
    open_weather_token=config.open_weather_token
    #city = data["name"] <-- если не лень то это надо пофиксить
    code_to_status = {
        "Clear" : 'ясная',
        "Clouds" : 'облачная',
        "Rain" : 'дождь',
        "Drizzle" : 'ливень',
        "Thunderstorm" : 'гроза',
        "Snow" : 'снег',
        "Mist" : 'туманно'
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )

        data = r.json()

        cur_weather = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        

        weather_status = data["weather"][0]["main"]

        if weather_status in code_to_status:
            ws = code_to_status[weather_status]
        else:
            ws = "я не могу понять погоду. посмотрите в окно."
        
        print('cheked: weather')
        to_say = f"В москве сейчас:, {num2words(int(cur_weather), lang='ru')} градусов по ц+е+льсию, но ощущается как {num2words(int(feels_like), lang='ru')}."

        if ws == code_to_status["Clouds"] or ws == code_to_status["Clear"]:
            to_say += f' Погода {ws}.'
        elif code_to_status["Rain"] or code_to_status["Drizzle"] or code_to_status["Thunderstorm"]:
            to_say += f' На улице {ws}.'

        to_say += f" Скорость ве+тра {num2words(int(wind), lang='ru')} метров в секунду. Давление {num2words(int(pressure), lang='ru')} паскаль."
        speak_ru(to_say)


    except Exception as ex:
        print(ex)
        print('Ошибка в погоде')


def gradus_weather(text_ru, text_en):
    city = config.CITY
    open_weather_token=config.open_weather_token
    code_to_status = {
        "Clear" : 'ясная',
        "Clouds" : 'облачная',
        "Rain" : 'дождь',
        "Drizzle" : 'ливень',
        "Thunderstorm" : 'гроза',
        "Snow" : 'снег',
        "Mist" : 'туманно'
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )

        data = r.json()

        cur_weather = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        

        weather_status = data["weather"][0]["main"]

        if weather_status in code_to_status:
            ws = code_to_status[weather_status]
        else:
            ws = "я не могу понять погоду. посмотрите в окно."
        
        print('cheked: weather')
        to_say = f"В москве сейчас:, {num2words(int(cur_weather), lang='ru')} градусов по ц+е+льсию, но ощущается как {num2words(int(feels_like), lang='ru')}."

        if ws == code_to_status["Clouds"] or ws == code_to_status["Clear"]:
            to_say += f' Погода {ws}.'
        elif code_to_status["Rain"] or code_to_status["Drizzle"] or code_to_status["Thunderstorm"]:
            to_say += f' На улице {ws}.'

        speak_ru(to_say)


    except Exception as ex:
        print(ex)
        print('Ошибка в погоде')


def web_search(text_ru, text_en):
    #Wolfram Alpha

    ban_ru_words = ['экспо', 'найди', 'винтернете', 'загугли', 'загугле', 'гугле']

    words = text_ru.split()
    c_words = [word for word in words if word.lower() not in ban_ru_words]
    text_ru = ' '.join(c_words)
    text_ru = text_ru.replace('в интернете', '', 1)

    url = f'https://yandex.ru/search/?text_ru={text_ru}'
    webbrowser.open_new_tab(url)


def calc(text_ru, text_en):
    speak_ru('команда в разработке.')


def convert(text_ru, text_en):
    speak_ru('команда в разработке.')



def translate_en(text_ru, text_en):
    def translate_text(text, target_language='en'):
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text


    ban_ru_words = ['экспо','эскпо', 'кспо', 'экспорт', 'экс', 'эксмо', 'экспорта', 'экстра',
                    'переведи', 'слово', 'слова',  'наанглийский', 'на', 'английский', 'на английский']

    words = text_ru.split()
    c_words = [word for word in words if word.lower() not in ban_ru_words]
    text_ru = ' '.join(c_words)

    target_language = 'en'  # Указываем 'ru' для перевода на русский язык
    translated_text = translate_text(text_ru, target_language)
    # translated_text = translated_text.replace('in English ', '').replace('into English', '')

    print(translated_text)
    speak_en(translated_text+'.')


def crypt(text_ru, text_en):
    ban_ru_words = ['текст', 'сообщение', 'строка', 'строку', 'зашифруй', 'расшифруй', 'слово']

    if 'зашифруй' or 'зашифровать' in text_ru.split():
        b = 'З'
    elif 'расшифруй' or 'расшифровать' in text_ru.split():
        b = 'Р'
    else:
        speak_ru('Упс... Кажется я в тупике. Попробуйте вызвать команду заново.')
        return 0

    a = text_ru

    for trig in words.TRIGGERS:
        if trig in a:
            a = a.replace(trig, '', 1)
    
    for ban in ban_ru_words:
        if ban in a:
            a = a.replace(ban, '', 1)


    def Z(a):
        s = ''
        for i in a:
            if i in alfabet:
                s += alfabet[i]
            else:
                s += i
        print('Полученнный текст:',s)

    def P(a):
        if ('предприм' in a) or ('инж' in a) or ('юр' in a) or ('лек' in a) or ('медиа' in a) or ('гж' in a) or ('академ' in a) or ('ит' in a) or ('акиб' in a) or ('АКАДЕМ' in a) or ('ИНЖ' in a) or ('ЮР' in a) or ('ЛЕК' in a) or ('МЕДИА' in a) or ('ГЖ' in a) or ('АКАДЕМ' in a) or ('ИТ' in a) or ('АКИБ' in a):
            while ('предприм' in a) or ('инж' in a) or ('юр' in a) or ('лек' in a) or ('медиа' in a) or ('гж' in a) or ('академ' in a) or ('ит' in a) or ('акиб' in a) or ('АКАДЕМ' in a) or ('ИНЖ' in a) or ('ЮР' in a) or ('ЛЕК' in a) or ('МЕДИА' in a) or ('ГЖ' in a) or ('АКАДЕМ' in a) or ('ИТ' in a) or ('АКИБ' in a):
                if ('предприм' in a):
                    a = a.replace('предприм', 'a', 1)
                if ('инж' in a):
                    a = a.replace('инж', 'б', 1)
                if ('юр' in a):
                    a = a.replace('юр', 'в', 1)
                if ('лек' in a):
                    a = a.replace('лек', 'г', 1)
                if ('медиа' in a):
                    a = a.replace('медиа', 'д', 1)
                if ('гж' in a):
                    a = a.replace('гж', 'к', 1)
                if ('академ' in a):
                    a = a.replace('академ', 'е', 1)
                if ('ит' in a):
                    a = a.replace('ит', 'я', 1)
                if ('акиб' in a):
                    a = a.replace('акиб', 'ж', 1)
                if ('ПРЕДПРИМ' in a):
                    a = a.replace('ПРЕДПРИМ', 'А', 1)
                if ('ИНЖ' in a):
                    a = a.replace('ИНЖ', 'Б', 1)
                if ('ЮР' in a):
                    a = a.replace('ЮР', 'В', 1)
                if ('ЛЕК' in a):
                    a = a.replace('ЛЕК', 'Г', 1)
                if ('МЕДИА' in a):
                    a = a.replace('МЕДИА', 'Д', 1)
                if ('ГЖ' in a):
                    a = a.replace('ГЖ', 'К', 1)
                if ('АКАДЕМ' in a):
                    a = a.replace('АКАДЕМ', 'Е', 1)
                if ('ИТ' in a):
                    a = a.replace('ИТ', 'Я', 1)
                if ('АКИБ' in a):
                    a = a.replace('АКИБ', 'Ж', 1)
            print('Полученнный текст:',a)


    alfabet = {
        'а': 'предприм',
        'б': 'инж', 
        'в': 'юр',
        'г': 'лек',
        'д': 'медиа',
        'к': 'гж',
        'е': 'академ', 
        'я': 'ит',
        'ж': 'акиб',
        'А': 'ПРЕДПРИМ',
        'Б': 'ИНЖ', 
        'В': 'ЮР',
        'Г': 'ЛЕК',
        'Д': 'МЕДИА',
        'К': 'ГЖ',
        'Е': 'АКАДЕМ', 
        'Я': 'ИТ',
        'Ж': 'АКИБ',
    }

    if b == 'З':
        Z(a)
        speak_ru('Сообщение зашифровано. Отправил результат в консоль.')
    elif b == 'Р':
        P(a)
        speak_ru('Сообщение расшифровано. Отправил результат в консоль.')


def de_desktop(text_ru, text_en):
    pyautogui.hotkey('winleft', 'd')
    time.sleep(1)

def de_volume(text_ru, text_en):
    def set_volume(device, volume_level):
        device.SetMasterVolumeLevelScalar(volume_level, None)

    def get_volume(device):
        return device.GetMasterVolumeLevelScalar()

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = get_volume(volume)
    vol_trans = {
        'ноль' : 0.0,
        'один' : 0.1,
        'два' : 0.2,
        'три' : 0.3,
        'четыре' : 0.4,
        'пять' : 0.5,
        'шесть' : 0.6,
        'семь' : 0.7,
        'восемь' : 0.8,
        'девять' : 0.9,
        'десять' : 1.0,
    }

    count_sovpad = 0
    for s_num, i_num in vol_trans.items():
        if s_num in text_ru.split():
            count_sovpad += 1
            check_var = i_num
    if count_sovpad == 1:
        new_volume = check_var
    elif count_sovpad < 1:
        speak_ru('Я могу выставлять гр+омкость только от одного до десяти.')
        new_volume = current_volume
    else:
        speak_ru('Для изменения гр+омкости на устройстве скажите, экспо, поставь громкость на два.')
        new_volume = current_volume


    # Установка громкости (от 0.0 до 1.0)
    set_volume(volume, new_volume)

    # Получение текущей громкости
    current_volume = get_volume(volume)
    print(f"Текущая громкость: {current_volume}")

def de_louder(text_ru, text_en):
    def set_volume(device, volume_level):
        device.SetMasterVolumeLevelScalar(volume_level, None)

    def get_volume(device):
        return device.GetMasterVolumeLevelScalar()
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = get_volume(volume)

    if current_volume < 1.0:
        new_volume = current_volume + 0.1
    else:
        speak_ru('Достигнут лимит громкости.')
        new_volume = current_volume

    # Установка громкости (от 0.0 до 1.0)
    set_volume(volume, new_volume)

    # Получение текущей громкости
    current_volume = get_volume(volume)
    print(f"Текущая громкость: {current_volume}")

def de_quieter(text_ru, text_en):
    def set_volume(device, volume_level):
        device.SetMasterVolumeLevelScalar(volume_level, None)

    def get_volume(device):
        return device.GetMasterVolumeLevelScalar()
    
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = get_volume(volume)

    if current_volume >= 0.1:
        new_volume = current_volume - 0.1
    elif 0.0 < current_volume < 0.1:
        new_volume = 0
    else:
        print('Достигнут лимит громкости.')
        new_volume = current_volume

    # Установка громкости (от 0.0 до 1.0)
    set_volume(volume, new_volume)

    # Получение текущей громкости
    current_volume = get_volume(volume)
    print(f"Текущая громкость: {current_volume}")


def execute_orders(text_ru, text_en):    
    def f1():
        speak_ru('Сейчас помогу вам сфокус+ироваться.')
        speak_ru('Команда в разработке.')

    def f2():
        speak_ru('Произвожу стандартный запуск.')
        speak_ru('Команда в разрботке.')

    def f3():
        pyautogui.hotkey('win', 'ctrl', 'd')
        time.sleep(1)
        def set_system_volume(volume):
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume_obj = cast(interface, POINTER(IAudioEndpointVolume))
            volume_obj.SetMasterVolumeLevelScalar(volume, None)
            
        speak_ru('Друг мой, вы в безопасности.')
        set_system_volume(0.0)


    def f4():
        print("Вызвана функция f4")

    def f5():
        print("Вызвана функция f5")

    def f6():
        print("Вызвана функция f6")

    def f7():
        print("Вызвана функция f7")

    def f8():
        print("Вызвана функция f8")

    def f9():
        print("Вызвана функция f9")

    def f10():
        print("Вызвана функция f10")

    number_dict = {
        'один': f1,
        'два': f2,
        'три': f3,
        'четыре': f4,
        'пять': f5,
        'шесть': f6,
        'семь': f7,
        'восемь': f8,
        'девять': f9,
        'десять': f10,
    }

    # Разбиваем введенную строку на слова
    words = text_ru.split()

    # Выбираем только слова, которые есть в словаре
    valid_words = [word for word in words if word in number_dict]

    # Проверяем, есть ли хотя бы одно допустимое слово
    if valid_words:
        # Вызываем соответствующую функцию по первому допустимому слову
        number_dict[valid_words[0]]()
    else:
        speak_ru('Что-то я в тупике. Попробуйте произнести запрос более чётко.')



def passive(text_ru, text_en):
    pass
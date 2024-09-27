import torch
import sounddevice as sd
import time




language = 'ru'
model_id = 'v3_1_ru' #ru_v3 | v3_1_ru
sample_rate = 48000
speaker = 'eugene' #aidar, baya, kseniya, xenia, eugene, random
device = torch.device('cpu') # gpu or cpu

model_speak, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)

model_speak.to(device)


def speak_ru(text: str):
    audio = model_speak.apply_tts(text=text,
                        speaker=speaker,
                        sample_rate=sample_rate)
    
    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()


# speak('текст является тэстовым. он отлично проверяет работоспособность голосовых связок.')
# speak_ru('привет. я голосовой виртуальный ассистент. меня зовут +экспо.')
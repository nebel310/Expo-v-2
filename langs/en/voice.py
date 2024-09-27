import torch
import sounddevice as sd
import time




language = 'en'
model_id = 'v3_en'
sample_rate = 48000
speaker = 'en_81' #en_110, en_111, !en_80, !en_81, en_13
device = torch.device('cpu') # gpu or cpu

model_speak, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)

model_speak.to(device)


def speak_en(text: str):
    audio = model_speak.apply_tts(text=text,
                        speaker=speaker,
                        sample_rate=sample_rate)
    
    sd.play(audio, sample_rate)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

# speak_en('the text is a test text. it perfectly checks the functioning of the vocal cords.')
# speak_en('hi. I am a voice virtual assistant. My name is +expo.')
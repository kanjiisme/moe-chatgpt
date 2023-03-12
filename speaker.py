from modules.models import SynthesizerTrn
import numpy as np
from scipy.io.wavfile import write
import pyaudio

model = SynthesizerTrn.from_pre_trained("model")

def to_16bit_audio(audio : np.ndarray):
    audio_samples = np.array(audio * (2**15 - 1), dtype=np.int16)

    return audio_samples

def to_speak(text, speaker_id = 0):
    
    rate, audio = model.to_speak(text, speaker_id)
    audio_samples = to_16bit_audio(audio)

    data = audio_samples.tobytes()

    return rate, data
    

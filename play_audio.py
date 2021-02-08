"""

import pyaudio
import wave

chunk = 1024

path = 'C://Users//03130//Desktop//2_석사//debate_audios//debate_audios//p1p2.wav'

with wave.open(path, 'rb') as f:
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)

    data = f.readframes(chunk)
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()
"""
#-*-coding : utf-8-*-

from playsound import playsound


playsound('path', True)

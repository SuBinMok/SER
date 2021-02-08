import soundfile as sf
import pytsmod as tsm
import numpy as np
#  https://stackoverflow.com/questions/22755558/increase-decrease-play-speed-of-a-wav-file-python/22761392


def pyts_mod(sound, octaves, x_length):
    s_ap = np.array([[0, x_length / 2, x_length], [0, x_length, x_length * 1.5]])
    x_s_fixed = tsm.wsola(sound, octaves)
    x_s_ap = tsm.wsola(sound, s_ap)

    x_s_ap = x_s_ap.T
    x_s_fixed =x_s_fixed.T

    return x_s_fixed, x_s_aps


def main():
    sound, sr = sf.read("path.wav")
    sound = sound.T
    sound_length = sound.shape[-1]

    s_fixed = 1.5 #(slow speed)
    #s_fixed = 0.5 #(fast speed)

    result1, result2 = pyts_mod(sound, s_fixed, sound_length)
    sf.write('./result/fast_result1.wav', result1, 44100)
    sf.write('./result/fast_result2.wav', result2, 44100)
    
if __name__ == '__main__':
    main()

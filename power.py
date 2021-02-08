'''
-*-*-*-*- 참고 -*-*-*-*-
https://hyunlee103.tistory.com/36
https://ahnjg.tistory.com/83
https://zuker.io/articles/2019-07/parselmouth-contour
https://hyongdoc.tistory.com/400
https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html
https://medium.com/swlh/visualising-speech-74137f0b793b

'''

import cv2
import time
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
import crepe
from scipy.io import wavfile
import sklearn
from librosa.core import pitch
import glob

def spectral(audio_path):
    print("-*-*-*-*-spectral-*-*-*-*-")
    #spectral centroid : centre of mass -- weighted mean of the frequendcies present in teh sound
    x, sr = librosa.load(audio_path)
    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
    spectral_shape = spectral_centroids.shape

    # Computing the time variable for visualization
    frames = range(len(spectral_centroids))
    t = librosa.frames_to_time(frames)

    librosa.display.waveplot(x, sr=sr, alpha = 0.4)
    plt.plot(t, nomalization(spectral_centroids), color='r')



def nomalization(x, axis = 0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)


def display_waveform(dir, fig_size):
    print("-*-*-*-*-display wave form-*-*-*-*-")
    Fig_Size = fig_size
    file = dir

    signal, sample_rate = librosa.load(file, sr=22050, res_type='audioread')
    print('signal shape : ', signal.shape)
    # plt.figure(figsize=Fig_Size)
    # librosa.display.waveplot(y=signal, sr=sample_rate, alpha=0.4)
    # plt.xlabel('time(s)')
    # plt.ylabel('Amplitude')
    # plt.title('wave form')
    # plt.show()

    return signal, sample_rate


def FFT(dir, fig_size): #power spectrum
    print("-*-*-*-*-FFT-*-*-*-*-")
    signal, sample_rate = display_waveform(dir, fig_size)
    fft = np.fft.fft()
    print('fft shape', fft.shape)

    spectrum = np.abs(fft)
    print('spectrum shape: ', spectrum.shape)

    f = np.linspace(0, signal, len(spectrum))
    print('f shape: ', f.shape)

    left_spectrum = spectrum[: int(len(spectrum)/2)]
    left_f = f[:int(len(spectrum)/2)]
    print('left_spectrum shape: ', left_spectrum.shape)
    print('left_spectrum shape: ', left_f)

    plt.figure(figsize=fig_size)
    plt.plot(left_f, left_spectrum, alpha=0.4)
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("Power spectrum")
    plt.savefig('./result.png', dpi=300)

def STFT(dir, fig_size):
    print("-*-*-*-*-STFT-*-*-*-*-")
    signal, sr = display_waveform(dir, fig_size)

    hop_length = 512  # total frame
    n_fft = 2048  # sample rate in a frame

    # calculate duration hop length and window in seconds
    hop_length_duration = float(hop_length) / sr
    n_fft_duration = float(n_fft) / sr

    stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)

    # 복소공간 값 절댓값 취하기
    magnitude = np.abs(stft)

    # magnitude > Decibels
    log_spectrogram = librosa.amplitude_to_db(magnitude) #dB

    # display spectrogram
    plt.figure(figsize=fig_size)
    librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram (dB)")
    # plt.savefig('stft15.png', dpi=300)
    return n_fft, hop_length

def mfcc(dir, fig_size):
    print("-*-*-*-*-MFCC-*-*-*-*-")
    signal, sr = display_waveform(dir, fig_size)
    n_fft, hop_length = STFT(dir, fig_size)

    MFCCs = librosa.feature.mfcc(signal, sr, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)

    # display MFCCs
    plt.figure(figsize=fig_size)
    librosa.display.specshow(MFCCs, sr=sr, hop_length=hop_length)
    plt.xlabel("Time")
    plt.ylabel("MFCC coefficients")
    plt.colorbar()
    plt.title("MFCCs")

    # show plots
    plt.savefig('./result.png', dpi=300)


def pitch_wave(path):
    """
    sr, audio = wavfile.read(path)
    time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
    print(time, frequency, confidence, activation)
    return(time, frequency, confidence, activation)
    """
    print("-*-*-*-*-pitch : wave.ver-*-*-*-*-")

    y, sr = librosa.load(path)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    plt.title("pitches")
    plt.plot(pitches)
    plt.show()

def pitch_spectro(path):
    print("-*-*-*-*-pitch : spectro.ver-*-*-*-*-")

    y, sr = librosa.load(path)
    S = np.abs(librosa.stft(y))
    pitches, magnitude = librosa.piptrack(S=S, sr=sr)
    plt.title("spectro pitches")
    plt.plot(pitches)
    plt.show()

def LowFrequency():
    print("-*-*-*-*-low frequency filter-*-*-*-*-")
    #주파수 추출 알고리즘

def HighFrequency():
    print("-*-*-*-*-high frequency filter-*-*-*-*-")
def frequency():
    print("-*-*-*-*-frequency-*-*-*-*-")
    #mean, max, median, SD

def ZCR():
    print("-*-*-*-*-ZCR-*-*-*-*-")

def PCA():
    print("-*-*-*-*-PCA-*-*-*-*-")

def amplitude():
    print("-*-*-*-*-amplitude-*-*-*-*-")

def main():
    dir = "path"
    
    
    # fs = (15, 10)
    pitch_spectro(dir)
    #https://groups.google.com/g/librosa/c/bR9wJwIzrrE?pli=1
    #https://newsight.tistory.com/336

if __name__ == '__main__':
    main()

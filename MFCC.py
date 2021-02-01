import matplotlib.pyplot as plt
import librosa.display
import librosa
import numpy as np



path = '##' #dir path
sample_rate = 16000 #sampling rate

'''
mfcc 순서
1. 해밍 윈도우를 통해 시간 정보가 있게 함.
2. spectrum(or spectrogram)을 구한다. 
    - 파일에 STFT를 취한다.
3. power normalized를 함.(생략 가능한듯)
    - power spectrum(or spectrogram)
4. Mel Filterbank를 적용한다.
    - Mel spectrum(or spectrogram)
5. log를 취하여 Log Mel spectrum(or spectrogram)을 구함
    - Log Mel spectrum(or spectrogram)
6. DCT를 적용함.
    - MFCC
'''
def mfcc(path, sample_rate):
    x = librosa.load(path, sample_rate)[0]#hamming와 STFT를 마침
    S = librosa.feature.melspectrogram(x, sr=sample_rate, n_mels = 128) #mel spectrum
    log_S = librosa.power_to_db(S, ref=np.max)#log mel sepctrum
    '''
        STFT를 마치면 time-amplitude 도메인에서 frequency-magnitude로 변하는데 
        magnitude에 log를 하여 dB로 바꾸면 색상 정보로 magnitude 정보를 표현하게 함. 
        이렇게 하면 frequency - time으로 다시 바뀌게 되어 시간 정보를 보존하고 분석할 수 있음.
    '''




    mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=20)#Mel-Frequency Cepstral 계수

    delta2_mfcc = librosa.feature.delta(mfcc, order=2)# 선택한 축을 따라 입력 데이터의 미분에 대한 로컬 추정.


    #visualization
    plt.figure(figsize=(12,4))
    librosa.display.specshow(delta2_mfcc)
    plt.ylabel('MFCC coefficients')
    plt.xlabel('Time')
    plt.title('MFCC')
    plt.colorbar()
    plt.tight_layout()
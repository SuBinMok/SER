import numpy as np
import matplotlib.pyplot as plt
import librosa

def calcu(data, sr, n_fft):
    data = data.astype(np.float) / 32767
    data = librosa.stft(data[sr // 4: sr // 4 * 2], n_fft=n_fft)
    data = np.mean(librosa.amplitude_to_db(np.abs(data)), axis=1)
    return data

def main():
    sr = 160000
    n_fft = 512

    data = np.fromfile("./result_audio/20210204/up_resynthesis.wav", dtype=np.int16)
    data2 = np.fromfile("./result_audio/20210204/l_u_resynthesis.wav", dtype=np.int16)
    data3 = np.fromfile("./result_audio/20210204/q_u_resynthesis.wav", dtype=np.int16)

    data = calcu(data, sr, n_fft)
    data2 = calcu(data2, sr, n_fft)
    data3 = calcu(data3, sr, n_fft)

    plt.title('total')

    plt.xlabel("Frequency[Hz]")
    plt.xticks(range(0, n_fft//2+1, 32), np.arange(0, 4001, 500))
    plt.xlim(0, n_fft//2)


    plt.ylabel("Amplitude[dB]")

    plt.plot(data, label='original', alpha=0.7)
    plt.plot(data2, label='louder', alpha=0.7)
    plt.plot(data3, label='quitter', alpha=0.7)
    plt.grid()
    plt.legend()

    fig = plt.gcf()

    plt.show()
    fig.savefig('./result_audio/20210204/up_total.png')

if __name__ == '__main__':
    # 감성 및 강도 입력받는 부분 만들기/
    main()
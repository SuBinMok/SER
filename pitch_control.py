
import parselmouth
from IPython.display import Audio
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from parselmouth.praat import call




def create_pitch(sound, pitch):
    manipulation = call(sound, "To Manipulation", 0.01,  20, 600)   #0.01초부터 시작되며, 20~600 Hz 범위를 가진다.
    pitch_tier = call("Create PitchTier", "name", 0,0.8)   #pitchTier를 0초에서 0.08까지 만든다.

    call(pitch_tier, "Add point", 0.01, 200)   #0.01초 포인트에서 100Hz로 만들어라.
    call(pitch_tier, "Add point", 1.5, 150)
    call(pitch_tier, "Add point", 2, 100)
    call(pitch_tier, "Add point", 3, 50)


    call([pitch_tier, manipulation], "Replace pitch tier")
    tone1Mod = call(manipulation, "Get resynthesis (overlap-add)")   #재합성 된 소리(pitch가 변함)
    Audio(data = tone1Mod.values, rate =tone1Mod.sampling_frequency)
    tone1Mod.save("./result/result.wav", "WAV")

    setupGraph(0, 300)
    plotOnGraph(tone1Mod.to_pitch(), 'r')
    plotOnGraph(pitch, 'b')
    plt.gca().legend(('resyn', 'original'))
    plt.savefig("./result/result.jpg")
    plt.show()



def plotOnGraph(pitch, color):
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize = 2.5, color = color)

def setupGraph(ymin, ymax):
    sns.set()
    plt.rcParams['figure.dpi']
    plt.figure()
    plt.ylim(ymin, ymax)
    plt.ylabel('frequency[Hz]')
    plt.xlabel('seconds')
    plt.grid(True)
    
def main():
    dir = 'Original.wav'
    sound = parselmouth.Sound(dir)
    Audio(data=sound.values, rate=sound.sampling_frequency)#play

    pitch = sound.to_pitch() #pitch extracted
   
    create_pitch(sound, pitch)

if __name__ == '__main__':
    main()

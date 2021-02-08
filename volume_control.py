#https://apple.stackexchange.com/questions/357436/how-can-i-determine-the-sound-volume-from-within-a-python-script

from pydub import AudioSegment

def volume(sound, dB):
    sound = sound + dB
    return sound

def main():
    dir = 'path'
    sound = AudioSegment.from_file(dir, format="mp3")
    louder = volume(sound, 20)

    # play(sound)
    # play(louder)
    louder.export("./result/result.wav", format= "wav")#export file


if __name__ == '__main__':
    main()

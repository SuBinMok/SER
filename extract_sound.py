import moviepy.editor as mp
import glob



path = "C:\\Users\\03130\\Videos\\4K Video Downloader\\test\\"

file_list = glob.glob(path+"\\*.mp4")
i=1
for file in file_list:

    clip = mp.VideoFileClip(file)
    clip.audio.write_audiofile(str(i) + ".mp3")
    i+=1
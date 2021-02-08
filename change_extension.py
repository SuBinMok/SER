from pydub import AudioSegment


dir = "KakaoTalk_Audio_20210202_1851_39_976.mp3"
sound = AudioSegment.from_file(dir, format="mp3")
sound.export("Original.wav", format="wav")  # export file


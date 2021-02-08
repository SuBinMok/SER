from pydub import AudioSegment


dir = "path"
sound = AudioSegment.from_file(dir, format="mp3")
sound.export("Original.wav", format="wav")  # export file

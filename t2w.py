import wikipedia
import pyttsx3
import os
f= open("tmp.tts","w+")
gh = wikipedia.page("Flat white")
text = gh.content
f.write(text)
f.close()
os.system("~/mimic -f tmp.tts -o tmp.wav")
os.system("ffmpeg -i tmp.wav -codec:a libmp3lame -qscale:a 2 output.mp3")
os.system("rm tmp.tts")
os.system("rm tmp.wav")

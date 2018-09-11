import os
def outmp3(text, fname="output"):
    f= open("tmp.tts","w+")
    f.write(text)
    f.close()
    os.system("~/mimic -f tmp.tts -o tmp.wav")
    os.system("ffmpeg -i tmp.wav -codec:a libmp3lame -qscale:a 2 {}.mp3".format(fname))
    os.system("rm tmp.tts")
    os.system("rm tmp.wav")

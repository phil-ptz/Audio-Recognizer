import sounddevice as sd
import wavio

fs = 44100

def record(sec):

    print('go')
    myrecording = sd.rec(int(sec * fs), samplerate=fs, channels=2)
    sd.wait()

    wavio.write('output.wav', myrecording, fs, sampwidth=2)
    print('stop')


# record()

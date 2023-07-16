import sounddevice 
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("SOUND RECORDING STARTED...!!!!")
    recording = sounddevice.rec((scounds * 44100), samplerate = 44100, channels = 2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("SOUND RECORDING FINISHED!!!")

voice_recorder(10, "record.wav")

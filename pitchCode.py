import vlc
import pyaudio
import sys
import aubio
import numpy as np
import math

def playNote(note):
	noteKey = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
	noteName = noteKey[note]
	song = "monsterNotes/" + noteName + ".aiff"
	p = vlc.MediaPlayer(song)
	p.play()
    

#all parameters should be indicies into the noteList
#noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
'''
-2nd interval = 2 half steps
-3rd interval = 4 half steps
-4th interval = 5 half steps
-5th interval = 7 half steps
-6th interval = 9 half steps 
-7th interval = 11 half steps
-octave = 12 half steps
'''
def checkInterval(interval, startingNote, sungNote):
    halfSteps = 0
    if(interval == 2):
        halfSteps = 2
    elif(interval <= 4):
        halfSteps = interval + 1
    elif(interval == 5):
        halfsteps = 7
    elif(interval == 6):
        halfSteps = 9
    elif(interval == 7):
        halfSteps = 11
    correctNote = (startingNote + halfSteps)%12
    if(sungNote == correctNote):
        return True
    return False


def hztoNote(hz):
    noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    A4 = 440
    C0 = int(A4*math.pow(2, -4.75))
    if(hz != 0):   
        h = int(12*math.log2(hz/C0))
        octave = h//12
        n = h%12
        return n
    return None

'''
p = pyaudio.PyAudio()

noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
buffer_size = 1024
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 44100
stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size)

tolerance = 0.8
win_s = 4096 # fft size
hop_s = buffer_size # hop size
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
pitch_o.set_unit("Hz")
pitch_o.set_tolerance(tolerance)

playNote(5)
'''

def record():
    p = pyaudio.PyAudio()

    noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    buffer_size = 1024
    pyaudio_format = pyaudio.paFloat32
    n_channels = 1
    samplerate = 44100
    stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size)
    tolerance = 0.8
    win_s = 4096 # fft size
    hop_s = buffer_size # hop size
    pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
    pitch_o.set_unit("Hz")
    pitch_o.set_tolerance(tolerance)
    audiobuffer = stream.read(buffer_size)
    signal = np.fromstring(audiobuffer, dtype=np.float32)

    pitch = pitch_o(signal)[0]
    confidence = pitch_o.get_confidence()
    #stream.stop_stream()
    #stream.close()
    #p.terminate()
    sungNote = hztoNote(pitch)
    if(sungNote != None):
        print(sungNote)
    return sungNote


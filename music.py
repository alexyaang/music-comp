import music21 as m21
from midiutil import MIDIFile
import numpy as np
import yfinance as yf
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
df = yf.download(tickers='MSFT', period = 'max', interval = '1d')
df['days'] = np.arange(len(df))

# Path: music.py
def get_notes():
    notes = []
    for i in df['Close']:
        notes.append(i)
    return notes

# create an algorithm to map 'MSFT' stock data with with midiutil
def create_midi(notes, filename):
    # create a MIDIFile object
    mf = MIDIFile(1)
    # add a track
    track = 0
    time = 0
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 120)
    channel = 0
    volume = 100
    for i in notes:
        pitch = i
        time = 0
        duration = 1
        mf.addNote(track, channel, pitch, time, duration, volume)
        time += 1
    with open(filename, 'wb') as outf:
        mf.writeFile(outf)

# create main function
def main():
    notes = get_notes()
    create_midi(notes, '~/Desktop/midi.mid')





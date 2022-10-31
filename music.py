import music21 as m21
from midiutil import MIDIFile
import numpy as np
import yfinance as yf
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
df = yf.download(tickers='MSFT', period = 'max', interval = '1d')
df['days'] = np.arange(len(df))









import example2 as vid
import scipy.io.wavfile as wavf
import get_freqs as four
import bode_plot as bplot
import pretty_plot as pplot

import numpy as np
import os

print("Check output mode: chained vs. superimposed")

f = raw_input("File to be transformed? ")
#f = ('notes')
plot = raw_input("Pretty, XKCD or Bode plot? Please type 'pretty','bode' or 'xkcd'.")

filterlist = raw_input("Filter names? Separate filters with a space.").split(' ')
#filterlist = ('high300.txt,low4000.txt').split(',')

filternames = {}
filtered_aud = {}

for item in filterlist:
	filternames[item] = []

rate, orig_aud = wavf.read(f+'.wav')
total_aud = orig_aud
sig = (str(f).split('.'))[0] 

path = sig + '_data'

if not os.path.exists(path):os.mkdir(path)

for name in filterlist:
	filtertext = (open('/filters'+name+'.txt', 'r').read()).split()

	for val in filtertext:
		if val != ' ':
			filternames[name].append(float(val))

	#Enable this to calculate the results of each filter evaluated separately
	filtered_aud[name] = np.convolve(filternames[name],orig_aud)
	four.get_freqs(filtered_aud[name],rate,sig,name)

	#Use this line to calculate the results of all filters chained together
	#total_aud = np.convolve(filternames[name],total_aud)

#Use this to see all filters chained
#four.get_freqs(total_aud,rate,sig,'total')

dirname, rate, interval = four.get_freqs(orig_aud,rate,sig,'base')

#Enable this to see the results of all filters superimposed on each other
to_plot = ['base'] + filternames.keys()

#Enable this to see the chained filter and the original data
#to_plot = ['base','total']

if plot == 'bode': bplot.make_bplot(dirname,to_plot)
elif plot == 'pretty': pplot.make_pplot(dirname,to_plot)
vid.make_video(dirname,plot)


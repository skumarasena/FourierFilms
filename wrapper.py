import example2 as vid
import scipy.io.wavfile as wavf
import get_freqs as four
import bode_plot as bplot
import pretty_plot as pplot

import numpy as np
import os

filterlist = []
filtertext = ""#string pulled from a filter
print("Check output mode: chained vs. superimposed")#program can either chain filters or make a plot with the results of each. 

f = raw_input("File to be transformed? ")
#f = ('notes')
plot = raw_input("Pretty or Bode plot? Please type 'pretty' or 'bode'.")

filterlist = raw_input("Filter names? Separate filters with a space.").split(' ')
#filterlist = ('high300.txt,low4000.txt').split(',')

if filterlist[0] == '':#avoids errors later in program if no filters are applied
	filterlist.pop(0)

filternames = {}#holds filter data
filtered_aud = {}#holds actual results

for item in filterlist:
	filternames[item] = []#used so that .append can be used later

rate, orig_aud = wavf.read(f+'.wav')
total_aud = orig_aud
sig = (str(f).split('.'))[0]#this is just the name of the file without the .wav extension

path = sig + '_data'

if not os.path.exists(path):os.mkdir(path)#makes a folder with the name "filename_data" in the current folder

for name in filterlist:
	filtertext = (open("Filters/IdealFilters/"+name+'.txt', 'r').read()).split()#splits the text of a filter into components

	for val in filtertext:
		if val != ' ':
			filternames[name].append(float(val))#adds numerical components of filter to a list for convolution

#Enable this to calculate the results of each filter evaluated separately
	filtered_aud[name] = np.convolve(filternames[name],orig_aud)
	four.get_freqs(filtered_aud[name],rate,sig,name)

#Use this line to calculate the results of all filters chained together
#total_aud = np.convolve(filternames[name],total_aud)

#Use this to see all filters chained
#four.get_freqs(total_aud,rate,sig,'total')

dirname, rate, interval = four.get_freqs(orig_aud,rate,sig,'base')

#wavf.write(sig+filterlist[0]+'.wav',rate, np.round(filtered_aud[filterlist[0]]*10000).astype('int16'))

#Enable this to see the results of all filters superimposed on each other
to_plot = ['base'] + filternames.keys()

#Enable this to see the chained filter and the original data
#to_plot = ['base','total']

if plot == 'bode': bplot.make_bplot(dirname,to_plot)
elif plot == 'pretty': pplot.make_pplot(dirname,to_plot)

vid.make_video(dirname,plot)

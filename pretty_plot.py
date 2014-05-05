"""
Opens a series of files and plots their content as a Bode plot. For use with the FourierFilms
project, due to specific filenaming conventions.

Emily Tumang, Samantha Kumarasena, Claire Keum
5/5/14
"""
import matplotlib.pyplot as plt
import numpy as np

def make_pplot(sig,to_plot):

	dirname = sig + '_data'

	freqs = {}
	phase = {}
	amp = {}
	colorlist = 'brg'

	#load data into dictionaries by filter name
	for name in to_plot:
		freqs[name] = np.load(dirname+'/'+name+'_freqs.npy')
		phase[name] = np.load(dirname+'/'+name+'_phase.npy')
		amp[name] = np.load(dirname+'/'+name+'_amp.npy') 

	xm = np.amax(freqs['base'])

	am = np.amax(amp['base'])

	pm = np.amax(phase['base'])
	pmi = np.amin(phase['base'])

	plt.autoscale(enable = False)

	for i in range(0,freqs['base'].shape[0]-1):

		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Magnitude')

		#create a bar plot, shifting the bars by 1/2 a bar width each time a new filter is applied
		for j in range(0, len(to_plot)):
			plt.bar(freqs[to_plot[j]][i]+2*j,amp[to_plot[j]][i],width = .5,label = to_plot[j],color = colorlist[j],edgecolor = colorlist[j])

		plt.ylim([0,am])
		plt.xlim([0,1000])

		plt.legend()

		plt.savefig(dirname+'/pretty'+str(i)+'.png')
		plt.clf()

if __name__=="__main__":
	make_bplot('notes',['base'])


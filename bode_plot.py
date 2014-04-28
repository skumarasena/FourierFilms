import matplotlib.pyplot as plt
import numpy as np

def make_bplot(sig,to_plot):

	dirname = sig + '_data'

	freqs = {}
	phase = {}
	amp = {}

	for name in to_plot:#todo... adapt this to multiple data sets
		freqs[name] = np.load(dirname+'/'+name+'_freqs.npy')
		phase[name] = np.load(dirname+'/'+name+'_phase.npy')
		amp[name] = np.load(dirname+'/'+name+'_amp.npy') 

	xm = np.amax(freqs['base'])

	am = np.amax(amp['base'])

	pm = np.amax(phase['base'])
	pmi = np.amin(phase['base'])

	plt.autoscale(enable = False)

	for i in range(0,freqs['base'].shape[0]-1):

		plt.subplot(211)
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Magnitude')

		for name in to_plot:
			plt.semilogx(freqs[name][i],amp[name][i],'.')

		plt.ylim([0,am])
		plt.xlim([0,xm])

		plt.subplot(212)
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Phase (rad)')


		for name in to_plot:
			plt.semilogx(freqs[name][i],phase[name][i])

		plt.ylim([pmi-1,pm+1])
		plt.xlim([0,xm])

		fig = plt.gcf()
		fig.subplots_adjust(hspace = .3)

		plt.savefig(dirname+'/bode'+str(i)+'.png')
		plt.clf()

if __name__=="__main__":
	make_bplot('notes',['base'])


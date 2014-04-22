import matplotlib.pyplot as plt
import numpy as np

def make_plot(dirname):
	
	freqs = np.load(dirname+'/freqs.npy')

	phase = np.load(dirname+'/phase.npy')

	amp = np.load(dirname+'/amp.npy')

	xm = np.amax(freqs)

	am = np.amax(amp)
	ami = np.amin(amp)

	pm = np.amax(phase)
	pmi = np.amin(phase)

	plt.autoscale(enable = False)

	for i in range(0,freqs.shape[0]-1):

		plt.subplot(211)
		plt.loglog(freqs[i],amp[i],'b.')
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Magnitude')
		plt.ylim([ami/100, am*10])
		plt.xlim([0,xm])

		plt.subplot(212)
		plt.semilogx(freqs[i],phase[i])
		plt.xlabel('Frequency (Hz)')
		plt.ylabel('Phase (rad)')
		plt.ylim([pmi-1,pm+1])
		plt.xlim([0,xm])

		fig = plt.gcf()
		fig.subplots_adjust(hspace = .3)

		plt.savefig(dirname+'/bode'+str(i)+'.png')
		plt.clf()

if __name__=="__main__":
	make_plot('notes_data',14400)
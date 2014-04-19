import scipy.io.wavfile as wavf
import numpy.fft as fourier
import numpy
import matplotlib.pyplot as plt
import os

PI = numpy.pi

#todo: shift things, filter things

f = 'music.wav'#replace this with the filepath of your desired sound
interval = .1 #must be <1

def get_freqs(file):
	rate, data = wavf.read(file)
	sig = (str(file).split('.'))[0]+"_"
	dirname = sig+'data'
	path = dirname+'/'
	plt.autoscale(enable = False)
	if not os.path.exists(dirname):os.mkdir(dirname)

	fft_data = []

	numstep = rate * interval

	for i in range(1, int(len(data)/numstep)):

		start = int((i-1)*numstep)
		stop = int((i)*numstep)

		a = fourier.fft(data[start:stop])
		mag = numpy.absolute(a[1:])
		freqs =abs(fourier.fftfreq(len(a[1:]),1.0/rate))
		angles = numpy.angle(a[1:])

		plt.plot(freqs,mag,'b.')
		plt.ylim([0,30000])# find a way to set this that isn't arbitrary...

		name = sig+str(i)

		plt.savefig(path+name+'.png')
		numpy.save(path+'freq'+str(i),freqs)
		#plt.show()
		plt.clf()

	#todo: put a copy of the .wav in the new folder, save the frequencies and amplitudes
	return dirname


get_freqs(f)

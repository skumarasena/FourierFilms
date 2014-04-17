import scipy.io.wavfile as wavf
import numpy.fft as fourier
import numpy
import matplotlib.pyplot as plt
import os

PI = numpy.pi

f = '21.wav'#replace this with the filepath of your desired sound
interval = .1 #must be <1

def get_freqs(file):
	rate, data = wavf.read(file)
	sig = (str(file).split('.'))[0]+"_"
	dirname = sig+'data'
	path = dirname+'/'
	if not os.path.exists(dirname):os.mkdir(dirname)

	fft_data = []

	numstep = rate * interval

	for i in range(1, int(len(data)/numstep)):

		start = int((i-1)*numstep)
		stop = int((i)*numstep)

		a = fourier.fft(data[start:stop])
		mag = numpy.absolute(a)
		img = a.imag
		freqs =abs(fourier.fftfreq(len(a),8000)/(2*PI))

		#plt.semilogy(freqs,mag,'b.')
		#plt.ylim([10^-1,10^7])

		name = sig+str(i)

		#plt.savefig(path+name+'.png')
		#plt.show()
		plt.clf()
		fft_data.append(a)

	print fft_data

	numpy.save(path+'data',data)
	numpy.append(path+'fft_results', fft_data)
		
get_freqs(f)


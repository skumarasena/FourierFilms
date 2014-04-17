import scipy.io.wavfile as wavf
import numpy.fft as fourier
import numpy
import matplotlib.pyplot as plt

PI = numpy.pi

f = '21.wav'#replace this with the filepath of your desired sound
interval = .1 #must be <1

def get_freqs(file):
	rate, data = wavf.read(file)
	sig = (str(file).split('.'))[0]+"_"

	numstep = rate * interval

	for i in range(1, int(len(data)/numstep)):

		start = int((i-1)*numstep)
		stop = int((i)*numstep)

		a = fourier.fft(data[start:stop])
		mag = numpy.absolute(a)
		img = a.imag
		freqs =abs(fourier.fftfreq(len(a),8000)/(2*PI))

		plt.semilogy(freqs,mag,'b.')
		plt.ylim([10^-1,10^7])

		name = sig+str(i)

		plt.savefig(name+'.png')
		#plt.show()
		plt.clf()

		
get_freqs(f)


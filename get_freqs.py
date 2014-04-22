import scipy.io.wavfile as wavf
import numpy.fft as fourier
import numpy as np
import os

PI = np.pi

file = 'notes.wav'

def get_freqs(file, interval = .1):
	rate, data = wavf.read(file)
	sig = (str(file).split('.'))[0] 
	dirname = sig+'_data'

	path = dirname + '/'

	if not os.path.exists(dirname):os.mkdir(dirname)

	numstep = rate*interval

	len_row = int(numstep-1)#-1 is to account for the removal of 0
	num_rows = int(len(data)/numstep)-2#-1 because we go from 1 in loop

	freq_array = np.zeros((num_rows,len_row))
	amp_array = np.zeros((num_rows,len_row))
	phase_array = np.zeros((num_rows,len_row))

	for i in range(1, num_rows):

		start = int((i-1)*numstep)
		stop = int((i)*numstep)

		a = fourier.fft(data[start:stop])
		mag = np.absolute(a[1:])
		freqs = abs(fourier.fftfreq(len(a[1:]),1.0/rate))
		angles = np.angle(a[1:])

		freq_array[i-1] = freqs
		amp_array[i-1] = mag
		phase_array[i-1] = angles

	np.save(path+'freqs.npy',freq_array)
	np.save(path+'amp.npy',amp_array)
	np.save(path+'phase.npy',phase_array)

	return (dirname, rate, interval)

if __name__=="__main__":
	print get_freqs(file)


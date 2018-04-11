# with some help from https://stackoverflow.com/questions/47954034/plotting-spectrogram-in-audio-analysis
import scipy
from scipy import signal
import scipy.io
import scipy.io.wavfile
import matplotlib
import matplotlib.pyplot as plt
#from matplotlib.pyplot import colormesh

# Read the .wav file
thelist = ["hello", "yes", "no", "hi", "shift"]
counts = 1
for i in thelist:
	counts = 1

	while counts < 11:

		sample_rate, data = scipy.io.wavfile.read('./' + i + str(counts) + '.wav')



		# Spectrogram of .wav file
		data *= 5
		sample_freq, segment_time, spec_data = signal.spectrogram(data, sample_rate)

		# Note sample_rate and sampling frequency values are same but theoretically they are different measures

		plt.figure(figsize=(2,2))

		plt.pcolormesh(segment_time, sample_freq, spec_data)
		#plt.tight_layout()
		plt.ylabel('Freq Hz')

		plt.axis('off')
		#plt.xlabel('time: sec')
		plt.savefig(i + str(counts)) #, dpi = (100))
		counts += 1
		plt.close()
		#plt.show()




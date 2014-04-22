import get_freqs as four
import bode_plot as bplot

file = raw_input("File to be transformed?")
dirname, rate, interval = four.get_freqs(file)
bplot.make_plot(dirname)

import get_freqs as four
import bode_plot as bplot
import pretty_plot as pplot
import example2 as vid

file = raw_input("File to be transformed? ")
type = raw_input("Pretty, XKCD or Bode plot? Please type 'pretty','bode' or 'xkcd'.")
dirname, rate, interval = four.get_freqs(file)

plot = type.lower()

if plot == 'bode': bplot.make_bplot(dirname)
elif plot == 'pretty': pplot.make_pplot(dirname)#this doesn't work, pplot not real

vid.make_video(dirname,plot)


#!/usr/bin/python
#
# Josh Lifton 2004
#
# Permission is hereby granted to use and abuse this document
# so long as proper attribution is given.
#
# This Python script demonstrates how to use the numarray package
# to generate and handle large arrays of data and how to use the
# matplotlib package to generate plots from the data and then save
# those plots as images.  These images are then stitched together
# by Mencoder to create a movie of the plotted data.  This script
# is for demonstration purposes only and is not intended to be
# for general use.  In particular, you will likely need to modify
# the script to suit your own needs.
#

from __future__ import print_function

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt   # For plotting graphs.
import numpy as np
import subprocess                 # For issuing commands to the OS.
import os
import sys                        # For determining the Python version.

#
# Print the version information for the machine, OS,
# Python interpreter, and matplotlib.  The version of
# Mencoder is printed when it is called.
#
# print('Executing on', os.uname())
# print('Python version', sys.version)
# print('matplotlib version', matplotlib.__version__)

# not_found_msg = """
# The mencoder command was not found;
# mencoder is used by this script to make an avi file from a set of pngs.
# It is typically not installed by default on linux distros because of
# legal restrictions, but it is widely available.
# """

# try:
#     subprocess.check_call(['mencoder'])
# except subprocess.CalledProcessError:
#     print("mencoder command was found")
#     pass # mencoder is found, but returns non-zero exit as expected
#     # This is a quick and dirty check; it leaves some spurious output
#     # for the user to puzzle over.
# except OSError:
#     print(not_found_msg)
#     sys.exit("quitting\n")



#
# Now that we have graphed images of the dataset, we will stitch them
# together using Mencoder to create a movie.  Each image will become
# a single frame in the movie.
#
# We want to use Python to make what would normally be a command line
# call to Mencoder.  Specifically, the command line call we want to
# emulate is (without the initial '#'):
# mencoder mf://*.png -mf type=png:w=800:h=600:fps=25 -ovc lavc -lavcopts vcodec=mpeg4 -oac copy -o output.avi
# See the MPlayer and MEncoder documentation for details.
#

# Figured out how to swap in a filepath... Now do this with user input. That would be cool.
# Also got audio working.
def make_video(name, plot_type):

    path = "mf://" + name + '_data/' + plot_type + '*.png'
    filename = name + '.wav'
    video = name + '.avi'

    command = ('mencoder',
           #'mf://notes_data/bode*.png',
           path,
           '-mf',
           'type=png:w=800:h=600:fps=12',
           '-ovc',
           'lavc',
           '-lavcopts',
           'vcodec=mpeg4',
           '-oac',
           'copy',
           '-o',
           video,
           '-audiofile',
           #'notes.wav', 
           filename,
           '-mc', 
           '0', 
           '-noskip')

    #os.spawnvp(os.P_WAIT, 'mencoder', command)

    print("\n\nabout to execute:\n%s\n\n" % ' '.join(command))
    subprocess.check_call(command)

    #change the name of the movie file so we can make a distinction!


    print("\n\n The movie was written to %s.avi" %name)

    print("\n\n You may want to delete %s*.png now.\n\n" %plot_type)


def main():
    make_video('notes', 'bode')

if __name__ == "__main__":
    main()
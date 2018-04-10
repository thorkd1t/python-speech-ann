# python-speech-ann # intended for one person to train and use, not a one fits all (i have not tested this)
Experimentation with neural networks and speech using python

This is the result of my experiments with Michael Wayman's (https://github.com/michaelwayman/python-ann) implementation of a digit recognition artificial neural network in python.

I ran this on linux with python 2.7, audnet.py looks for the specified spectrogram image file, then read the rgb values of each pixel and feed this into the neural network

soun.py when run will record audio to wav (on linux with jack_control installed)
ideally run soun.py and speak the same word ten times making sure to leave a small silence between them, then split these up with something like audacity into their own wavs named as such: hello1.wav through hello10.wav, yes1.wav through yes10.wav
the program is setup to read 10 wav files for each word in wordlist, it then trains with 6 of each of them and tests with the remaining 4.
basically you need 10 wav files for each word in wordlist, or you could change the program of course
sigh.py turns wav files into spectrogram

I am by no means experienced with neural networks especially and I was actually expecting this to require a lot more training, however once the blue from the rgb values had been ignored, and white in the spectrogram was zeroed, it became very accurate very fast (unless I am very much mistaken which is very possible) if anyone has any insight into this i would be very interested to hear it

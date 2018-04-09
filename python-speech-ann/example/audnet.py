import matplotlib.pyplot as plt
from Tkinter import *
import sys, os
import numpy
import time
import scipy
from scipy import signal
from scipy.io import wavfile
import matplotlib.image as mpimg
from Tkinter import *
import Tkinter as tk
master = tk.Tk()

# thanks to https://github.com/michaelwayman/python-ann
# and people on stackoverflow
# Sloppily add neural_network to our path so we can import it
sys.path.insert(0, os.path.abspath('../neural_network'))
wordlist = ["hello","yes","no", "hi", "shift"] # used to queue up the files needed

from neural_network import NeuralNet # import Michael Wayman's neural net

ti = time.time() # log start time

def getRGB(image, x, y): # function for getting the rgb values of each pixel of the spectrogram
    value = image.get(x, y)

    return tuple(map(int, value)) #changed value.split(" ") to value


def train_the_neural_net(neural_net, epochs):

    print 'Training the neural network.'

    epochs = epochs # times to repeat the training
    countin = 1 # counter for file loop
    eps = 1 # to keep track of the epochs
    
    for i in range(epochs):
        print 'epoch ' + str(eps)
        eps += 1

        for i in wordlist: # for each word ie hello, hi
            countin = 1
            while countin < 7: # loop through files 1-6
                #hm = 0
                #master.geometry("200x200")
                hum = tk.PhotoImage(file= i + str(countin) +  ".png") # get a pixel map
                count1 = 0

                count2 = 0
                flotar = [] # array to hold the values of the pixels
                while count1 < 200: # loop through x axis 
                    
                    if count2 == 200: # end of this row/col so reset ready for next
                            count2 = 0
                            
                    while count2 < 200: # loop through y axis

                        a, b, c = getRGB(hum, count1, count2) # save the r,g,b valuesm of this pixel

                        if a == 255: # if
                            if b == 255: # its
                                if c == 255: # white, set to 0
                                    a = 0
                                    b = 0
                                    c = 0

                        flotar.append(a) # append red
                        flotar.append(b) # append green                        
                        #flotar.append(c) # worked a LOT better after ignoring blue and zeroing all white px
                        count2 += 1                                    
                    count1 += 1
                         
                imag = (numpy.asfarray(flotar) / 255 * 0.99) + 0.01 # make a numpy array with all the r and g pix data
                     
                targets = numpy.zeros(output_nodes) + 0.01 # reset the targets

                if i == "hello": targets[0] = 0.99 # set target
                elif i == "yes": targets[1] = 0.99
                elif i == "no": targets[2] = 0.99
                elif i == "hi": targets[3] = 0.99
                elif i == "shift": targets[4] = 0.99

                neural_net.train(imag, targets) # train with this image data
                countin += 1
                flotar = "" # reset float array for next run

        print 'complete.'

def test_the_neural_net(neural_net):
    print 'Testing the neural network.'
    scorecard = [] # to determine how accurate the test was 1 == correct 0 == false
    for i in wordlist:


        countin = 7

        hum = tk.PhotoImage(file= i + str(countin) +  ".png")
        
        while countin < 11:

            count1 = 0
            count2 = 0
            flotar = []
            while count1 < 200:
                #print count1
                if count2 == 200: 
                        count2 = 0
                        
                while count2 < 200:
                    a, b, c = getRGB(hum, count1, count2)
                        
                    if a == 255:
                        if b == 255:
                            if c == 255:
                                a = 0
                                b = 0
                                c = 0
                    flotar.append(a)
                    flotar.append(b)
                    if a != 255 and b != 255 and c != 255:
                        if a != 0 and b != 0:
                            print str(a) + " " + str(b) + " " + str(c)
                    #time.sleep(0.05)
                    #if c == 255: c = 0
                    #flotar.append(c)
                    count2 += 1
                                        
                count1 += 1

                          
            imag = (numpy.asfarray(flotar) / 255 * 0.99) + 0.01
                     
            targets = numpy.zeros(output_nodes) + 0.01

            if i == "hello":
                targets[0] = 0.99
            elif i == "yes":

                targets[1] = 0.99
            elif i == "no":
                targets[2] = 0.99
            elif i == "hi":
                targets[3] = 0.99
            elif i == "shift":
                targets[4] = 0.99

            neural_net.train(imag, targets)
            if i == "hello":
                correct_label = 0
            elif i == "yes":
                correct_label = 1
            elif i == "no":
                correct_label = 2
            elif i == "hi":
                correct_label = 3
            elif i == "shift":
                correct_label = 4
            
            outputs = neural_net.query(imag)
            label = numpy.argmax(outputs)
            if label == correct_label:
                scorecard.append(1)
                print "correct " + str(label)
            else:
                scorecard.append(0)
                print str(i) + " failed thought it was " + str(label) + " file is number " + str(countin)



            countin += 1
            flotar = ""






    print 'complete.'
    print scorecard
    return scorecard

if __name__ == '__main__':

    print 'Starting neural network to recognize audio... maybe....'

    input_nodes = 80000 # 200x200 pixel image == 40,000 pixels, each px has red + green values to save so we need 80k
    hidden_nodes = 185 
    output_nodes = 10 # 0 == hello, 1 == yes, 2 == no
    learning_rate = 0.1

    nn = NeuralNet(input_nodes, hidden_nodes, output_nodes, learning_rate)

    # Train
    train_the_neural_net(nn, epochs=1)
    # Test
    test_results = numpy.asarray(test_the_neural_net(nn))

    # Print results
    print('Neural network is {}% accurate at predicting audio.... maybe....'
        .format(test_results.sum() / float(test_results.size) * 100.0))
    thyme = time.time()
    thyme -= ti
    print str(thyme) + " seconds"


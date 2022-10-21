#import csv
import os
import matplotlib.pyplot as plt

def graph(d, x_label, y_label):
    # graphs the frequencies based on the dictionary
    plt.scatter(d.keys(), d.values(), linewidth=0)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def freq(input_file):
    # reads the input file and gets the frequency of each letter. Returns a dictionary with the frequencies.
    if os.path.isfile(input_file) == False:
        print("Error: Input file not found. Please enter a valid file.") # message should be shown in GUI
        return {}
    with open(input_file, 'r') as inf:
        frequency = {}
        s = inf.read().upper()
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency


# main program
'''fn = input("Enter the file name: ") # this should be done in GUI part
print("Loading . . .")
f = freq(fn) # gets the frequency of all characters as a dictionary
writefreq(f, "freqfile.csv") # writes it to a csv file
xy = load_from_csv("freqfile.csv") # loads from the csv file
graph(xy[0],xy[1], "Character", "No. of occurences") # graphing'''

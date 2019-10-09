#!/usr/bin/python3
import sys
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import locale
import argparse
import csv
import os.path

from os import path


def projection(monthlyContribution, duration, growth, platformFee, platformCap, fundFee):
    total = 0
    stats = []

    stats.append(0) 
    for year in range(0, duration):
        total = total + (monthlyContribution*12)
        # Adding expected growth 
        total = total * (1+(growth/100))
        # Working out the fund fee 
        fundFees = total * (fundFee/100)
        # Working out the platform fee and make sure it isn't over the cap.
        platformFees = total * (platformFee/100)
        if platformFees > platformCap :
            platformFees = platformCap
 
        total = total - platformFees - fundFees
        stats.append(total)
  
    return stats

def main(argv):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--input', required=True, type=str, help='The CSV file to plot the data from.')
    args = parser.parse_args()

    if not path.isfile(args.input):
        print("The input CSV file '{}' does not exist or is not a file.".format(args.input))
        sys.exit(2)

    with open(args.input) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            investment = (projection(float(row[0]), int(row[1]), float(row[2]), float(row[3]), float(row[4]) , float(row[5]))); 
            plt.plot(range(0, int(row[1])+1), investment, color='green')
 
    plt.xlabel('Duration (Years)')
    plt.ylabel('Total ($)')
    plt.grid(True)  
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])

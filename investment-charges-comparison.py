#!/usr/bin/python3
import sys
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import locale
import argparse
import csv
import os.path

from os import path

locale.setlocale(locale.LC_ALL, '')


def projection(monthly_contribution, duration, growth, platform_fee,
               platform_cap, fund_fee):
    total = 0
    stats = []

    stats.append(0)
    for year in range(0, duration):
        total = total + (monthly_contribution*12)
        # Adding expected growth
        total = total * (1+(growth/100))
        # Working out the fund fee
        fund_fees = total * (fund_fee/100)
        # Working out the platform fee and make sure it isn't over the cap.
        platform_fees = total * (platform_fee/100)
        if platform_fees > platform_cap:
            platform_fees = platform_cap

        total = total - platform_fees - fund_fees
        stats.append(total)

    return stats


def main(argv):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-i', '--input', required=True, type=str,
                        help='The CSV file to plot the data from.')
    args = parser.parse_args()

    if not path.isfile(args.input):
        print("The input CSV file '{}' does not exist or is not a file."
              .format(args.input))
        sys.exit(2)

    patches = []

    with open(args.input) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if len(row) == 8:
                investment = (projection(float(row[2]), int(row[3]),
                              float(row[4]), float(row[5]), float(row[6]),
                              float(row[7])))
                plt.plot(range(0, int(row[3])+1), investment,
                         color=str(row[1]).strip())
                temp_label = str(row[0]).strip()+' Total : '+
                                    str(locale.currency(investment[len(investment)-1],
                                    grouping=True))
                temp_patch = mpatches.Patch(color=str(row[1]).strip(), label=temp_label)
                patches.append(temp_patch)
            else:
                print("CSV row not in the expected format.")
                print(row)
                print("Expected Format : Name, Colour, Monthly Contribution, Duration, Growth, Platform Fee, Platform Cap, Fund Fee")

    plt.legend(handles=patches)
    plt.xlabel('Duration (Years)')
    plt.ylabel('Total ($)')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])

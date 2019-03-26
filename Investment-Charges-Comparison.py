#!/bin/python
import sys
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import locale

locale.setlocale( locale.LC_ALL, '' )
years = range(0, int(sys.argv[2])+1)

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

investment1 = (projection(float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]) , float(sys.argv[6])));

investment2 = (projection(float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[7]), float(sys.argv[8]) , float(sys.argv[9])));

plt.plot(years, investment1, color='red')
plt.plot(years, investment2, color='blue')
plt.xlabel('Duration (Years)')
plt.ylabel('Total (£)')
plt.grid(True)
red_label = 'Total : '+str(locale.currency(investment1[len(investment1)-1], grouping=True ))
blue_label = 'Total : '+str(locale.currency(investment2[len(investment2)-1], grouping=True ))
red_patch = mpatches.Patch(color='red', label=red_label)
blue_patch = mpatches.Patch(color='blue', label=blue_label)
plt.legend(handles=[blue_patch, red_patch])
plt.show()

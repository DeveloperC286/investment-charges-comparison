#!/bin/python
import sys
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import locale

locale.setlocale( locale.LC_ALL, '' )
years = range(0, int(sys.argv[2]))

def projection(monthlyContribution, duration, TER, yearlyGrowth):
    total = 0
    stats = []
    
    for year in range(0, duration):
        stats.append(total)
        total = total + (monthlyContribution*12)
        # Adding expected growth 
        total = total * (1+(yearlyGrowth/100))
        # Subtracting total expense ration (TER)
        total = total * (1-(TER/100))
    
    return stats

investment1 = (projection(float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])));
investment2 = (projection(float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[5]), float(sys.argv[6])));

plt.plot(years, investment1, color='red')
plt.plot(years, investment2, color='blue')
plt.xlabel('Duration (Years)')
plt.ylabel('Total (£)')
plt.grid(True)
red_label = 'Total : '+str(locale.currency(investment1[len(investment1)-1], grouping=True ))+', Projected Growth : '+sys.argv[4]+'%, TER : '+sys.argv[3]+'%'
blue_label = 'Total : '+str(locale.currency(investment2[len(investment2)-1], grouping=True ))+', Projected Growth : '+sys.argv[6]+'%, TER : '+sys.argv[5]+'%'
red_patch = mpatches.Patch(color='red', label=red_label)
blue_patch = mpatches.Patch(color='blue', label=blue_label)
plt.legend(handles=[blue_patch, red_patch])
plt.show()

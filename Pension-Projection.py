#!/bin/python
import sys
import matplotlib.pyplot as plt

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

plt.plot(years, investment1)
plt.plot(years, investment2)
plt.xlabel('Duration (Years)')
plt.ylabel('Total (£)')
plt.grid(True)
plt.show()

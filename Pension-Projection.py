#!/bin/python
import locale
import sys

locale.setlocale( locale.LC_ALL, '' )

def projection(monthlyContribution, duration, TER, yearlyGrowth):
    total = 0 
    
    for year in range(0, duration):
        total = total + (monthlyContribution*12)
        # Adding expected growth 
        total = total * (1+(yearlyGrowth/100))
        # Subtracting total expense ration (TER)
        total = total * (1-(TER/100))
    return total

print("-- Constants --")
print("Monthly Contribution: ",float(sys.argv[1]))
print("Duration: ",int(sys.argv[2]))
print("")
print("-- Investment 1 --")
print("Total: ", locale.currency(projection(float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])), grouping=True));
print("Expected Growth: ",sys.argv[4],"%")
print("Total Charges: ",sys.argv[3],"%")
print("")
print("-- Investment 2 --")
print("Total: ", locale.currency(projection(float(sys.argv[1]), int(sys.argv[2]), float(sys.argv[5]), float(sys.argv[6])), grouping=True));
print("Expected Growth: ",sys.argv[6],"%")
print("Total Charges: ",sys.argv[5],"%")


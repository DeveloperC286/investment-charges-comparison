#!/bin/python
import locale

def projection(monthlyContribution, duration, TER, yearlyGrowth):
    total = 0 
    
    for year in range(0, duration):
        total = total + (monthlyContribution*12)
        # Adding expected growth 
        total = total * (1+(yearlyGrowth/100))
        # Subtracting total expense ration (TER)
        total = total * (1-(TER/100))
    return total

locale.setlocale( locale.LC_ALL, '' )
print ("\nTotal -\n", locale.currency(projection(100,35,1.25,8), grouping=True));

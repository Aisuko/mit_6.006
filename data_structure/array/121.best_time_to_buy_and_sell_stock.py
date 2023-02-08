#!/usr/bin/env python
#Array
#dynamic programming


def maxProfit(prices)->int:
    finalProfit=profit=k=0
    
    while k<len(prices)-1:
        # Here we do not need to iterater every elements twice, please remember that the profit=(yesterday's profit+today's profit)
        # the latest profit= total profit until now compares to today's profit
        profit=max(0,profit+prices[k+1]-prices[k])
        finalProfit=max(profit,finalProfit)
        k+=1
    return finalProfit

print(maxProfit([7,1,5,3,6,4]))

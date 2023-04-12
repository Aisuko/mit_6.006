#!/usr/bin/env python
#Array
#dynamic programming
# O(n)

def maxProfit(prices)->int:
    """121. Best time to but and sell stock

    Time complexity: I assumed it is O(n), n=len(prices)-1
    """
    finalProfit=profit=k=0
    
    while k<len(prices)-1:
        # Here we do not need to traversal every elements twice, please remember that the profit=(yesterday's profit+today's profit)
        # the latest profit= total profit until now compares to today's profit

        # In this case, the minimal profit is 0. So, it will be wrong if you use max (temp,temp+today's profit)
        profit=max(0,profit+prices[k+1]-prices[k])
        finalProfit=max(profit,finalProfit)
        k+=1
    return finalProfit

# print(maxProfit([7,1,5,3,6,4]))

if __name__=="__main__":
    print(maxProfit([7,1,5,3,6,4]))
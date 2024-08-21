# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices: list[int]) -> int:
    profit = 0
    mini = prices[0]
    for i in range(len(prices)):
        mini = min(mini,prices[i])
        profit = max(profit, prices[i]-mini)
    return profit

    # min = 0
    #for i in range(len(prices)):
        

    # max = min
    # for j in range(min,len(prices)):
    #     if prices[j] > prices[max]:
    #         max = j
    
    # if min < max:
    #     return prices[max] - prices[min]
    # return 0

print(maxProfit([3,3,5,0,0,3,1,4]))
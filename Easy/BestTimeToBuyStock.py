# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices: list[int]) -> int:
    profit = 0
    mini = prices[0]
    for i in range(len(prices)):
        mini = min(mini,prices[i])
        profit = max(profit, prices[i]-mini)
    return profit
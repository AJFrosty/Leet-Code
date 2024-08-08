# https://leetcode.com/problems/buy-two-chocolates

class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        best = [0,0]
        bProfit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if (prices[i]+prices[j]) <= money:
                    profit = (money -(prices[i]+prices[j]))
                    if profit >= bProfit:
                        bProfit = profit
                        best = [prices[i],prices[j]]
        return money - (best[0]+best[1])
    
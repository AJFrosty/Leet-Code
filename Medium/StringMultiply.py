# https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = ["0","1","2","3","4","5","6","7","8","9"]
        prod = 0
        
        power = len(num1)-1

        for x in num1:
            prod += nums.index(x) * (10**power)
            power -= 1
        
        power = len(num2)-1
        sumNum = 0
        for y in num2:
            sumNum += nums.index(y) * (10**power)
            power -= 1
        prod *= sumNum
        
        return str(prod)
        
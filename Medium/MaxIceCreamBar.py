# https://leetcode.com/problems/maximum-ice-cream-bars/description/
def maxIceCream(costs: list[int], coins: int) -> int:
    costs.sort()
    count = 0

    for i in range(len(costs)):
        if coins >= costs[i]:
            count += 1
            coins -= costs[i]
    return count

print(maxIceCream([10,6,8,7,7,8],5))

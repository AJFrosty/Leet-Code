# https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/
class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) ->list[int]:
        answer = []
        odd = 0

        for i in range(len(nums)):
            if nums[i]%2 == 1:
                odd += nums[i]
        
        for i in range(len(nums)):
            ans = nums[queries[i][1]]+queries[i][0]
                
            if ans%2 == 0 and nums[queries[i][1]] %2 == 1:
                odd -= nums[queries[i][1]]
                nums[queries[i][1]] += queries[i][0]
                answer.append(sum(nums)-odd)

            elif ans%2 == 1 and nums[queries[i][1]] %2 == 1:
                odd += ans-nums[queries[i][1]]
                nums[queries[i][1]] += queries[i][0]
                answer.append(sum(nums)-odd)

            elif ans%2 == 1:
                odd += ans
                nums[queries[i][1]] += queries[i][0]
                answer.append(sum(nums)-odd)

            else:
                nums[queries[i][1]] += queries[i][0]
                answer.append(sum(nums)-odd)

        return answer
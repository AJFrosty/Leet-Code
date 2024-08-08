# https://leetcode.com/problems/product-of-array-except-self/

# class Solution(object):
#     def productExceptSelf(self, nums):
#         pred = [1]*len(nums)
#         suc = [1]*len(nums)
#         answer = [1]*len(nums)

#         product = 1
#         for i in range(len(nums)):
#             pred[i] = product
#             product *= nums[i]

#         product = 1
#         for i in range(len(nums)-1,-1,-1):
#             suc[i] = product
#             product *= nums[i]

#         for i in range(len(nums)):
#             answer[i] = pred[i] * suc[i]
#         return answer
def productExceptSelf(nums):
    pred = [1]*len(nums)
    suc = [1]*len(nums)
    answer = [1]*len(nums)

    product = 1
    for i in range(len(nums)):
        pred[i] = product
        product *= nums[i]

    product = 1
    for i in range(len(nums)-1,-1,-1):
        suc[i] = product
        product *= nums[i]

    for i in range(len(nums)):
        answer[i] = pred[i] * suc[i]
    return answer
print(productExceptSelf([1,2,3,4]))
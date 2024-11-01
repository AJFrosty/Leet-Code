# https://leetcode.com/problems/combination-sum/description/

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    final = []
    lengths = []

    for i in range(len(candidates)):
        count = target//candidates[i]
        rem = target % candidates[i]
        check = candidates[i]+rem

        if check in candidates:
            result = [candidates[i]]*(count-1)
            result.insert(0,check)
            if result not in final and len(result) not in lengths:
                final.append(result)
                lengths.append(len(result))

        if rem in candidates:
            result = [candidates[i]]*(count)
            result.insert(0,rem)
            if result not in final and len(result) not in lengths:
                final.append(result)
                lengths.append(len(result))
    
    return final

print(combinationSum([3,5,7],10))

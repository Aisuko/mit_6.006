def twoSum(nums, target):
    lenNums=len(nums)
    if lenNums==1:
        return nums[0]
    re={}
    for k,y in enumerate(nums):
        if target -y in re:
            return [re[target-y],k]
        else:
            re[y]=k


print(twoSum([2,7,11,15],9))
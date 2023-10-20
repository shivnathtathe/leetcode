class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        numsss=[]
        for i in range(len(nums)):
            if nums[i] == target:
                numsss.append(i)
        return numsss
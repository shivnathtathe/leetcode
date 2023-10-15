class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1
        #return min(nums)
        
        #2
        min_of = float('inf')
        for i in nums:
            current = i
            min_of = min(current,min_of)
        return min_of
        
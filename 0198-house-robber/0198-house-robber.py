class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b =0,0
        
        for i in nums:
            r = max(i+a,b)
            a = b
            b = r
        return b
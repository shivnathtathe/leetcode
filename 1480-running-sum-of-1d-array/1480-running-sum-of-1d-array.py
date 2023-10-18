class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list=[]
        
        current_sum = 0
        
        for i in nums:
            current_sum +=i
            new_list.append(current_sum)
        return new_list
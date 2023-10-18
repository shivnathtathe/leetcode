class Solution:
    def thirdMax(self, nums: List[int]) -> int:
     
        new_num = set(nums)
        list_new = list(new_num)
        list_new.sort()
        
        if len(list_new)<=2:
            return max(list_new)
        return list_new[-3]
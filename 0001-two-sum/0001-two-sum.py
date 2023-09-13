class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_dict = {}
        sum_tar = []

        for ptr1 in range(len(nums)):
            val = target - nums[ptr1]
            
            if val in value_dict:
                sum_tar.append(value_dict[val])
                sum_tar.append(ptr1)
                return sum_tar
            
            value_dict[nums[ptr1]] = ptr1

        return []


        



class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # element sum - digit sum
        element_sum = sum(nums)
        digit_sum =0
        new_str =''
        for i in nums:
            new_str += str(i)
        for j in new_str:
            digit_sum += int(j)
        return element_sum - digit_sum
            
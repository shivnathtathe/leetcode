class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1
        min_element = nums[0]

        for i in range(1, n):
            if nums[i] > min_element:
                max_diff = max(max_diff, nums[i] - min_element)
            else:
                min_element = nums[i]

        if max_diff == -1:
            return -1

        return max_diff


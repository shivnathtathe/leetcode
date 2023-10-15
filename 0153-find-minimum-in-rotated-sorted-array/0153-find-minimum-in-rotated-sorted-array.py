class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1
        #return min(nums)
        
        #2
        # min_of = float('inf')
        # for i in nums:
        #     current = i
        #     min_of = min(current,min_of)
        # return min_of
        
        #3
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        
#using collection module
import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for i,j in counter.items():
            if j > 1:
                return i
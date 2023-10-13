class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_list = []
        for i in nums1:
            if i in nums2:
                new_list.append(i)
        return list(set(new_list))
                    
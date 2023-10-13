class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         list1 = []
#         list2 =[]
#         final_list =[]
        
#         for i in nums1:
#             if i not in nums2:
#                 list1.append(int(i))
#         for j in nums2:
#             if j not in  nums1:
#                 list2.append(int(j))
#         final_list.append(list1)
#         final_list.append(list2)
#         return final_list
        
        
        set1 = set(nums1)
        set2 = set(nums2)

        list1 = list(set1 - set2)
        list2 = list(set2 - set1)

        final_list = [list1, list2]
        
        return final_list

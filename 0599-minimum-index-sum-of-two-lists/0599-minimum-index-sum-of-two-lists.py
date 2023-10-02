class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        min_sum = float('inf')

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    sum_num = i + j

                    if sum_num < min_sum:
                        min_sum = sum_num
                        common = [list1[i]]
                    elif sum_num == min_sum:
                        common.append(list1[i])

        return common

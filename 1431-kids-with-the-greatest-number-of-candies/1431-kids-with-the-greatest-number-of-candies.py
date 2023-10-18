class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_list =[]
        maximum = max(candies)
        for i in candies:
            if (i + extraCandies) >= maximum:
                new_list.append(True)
            else: 
                new_list.append(False)
        return new_list
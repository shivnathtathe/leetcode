class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_restaurants = []
        index_map = {}
        
        for i, restaurant in enumerate(list1):
            index_map[restaurant] = i
        
        min_sum = float('inf')
        
        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                sum_num = j + index_map[restaurant]
                
                if sum_num < min_sum:
                    min_sum = sum_num
                    common_restaurants = [restaurant]
                elif sum_num == min_sum:
                    common_restaurants.append(restaurant)

        return common_restaurants

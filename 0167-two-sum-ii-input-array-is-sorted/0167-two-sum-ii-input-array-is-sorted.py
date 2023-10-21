class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map ={}
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            if new_target in hash_map:
                return [hash_map[new_target]+1,i+1]
            hash_map[numbers[i]] = i
        return []
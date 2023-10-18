class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        remove_count = int(n * 0.05)
        
        trimmed_arr = arr[remove_count:n - remove_count]
    
    # Calculate the mean of the trimmed array
        mean = sum(trimmed_arr) / len(trimmed_arr)
    
        return mean
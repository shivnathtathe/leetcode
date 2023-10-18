class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 =nums[:n]
        list2 = nums[n:]
        
        demo =[]
        
        for i in range(0,len(list1)):
            demo.append(list1[i])
            demo.append(list2[i])
        return demo
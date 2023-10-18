class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        count = float('-inf')
        
        for i in range(len(accounts)):
            current_sum = sum(accounts[i])

            count = max(count,current_sum)
        return count
                
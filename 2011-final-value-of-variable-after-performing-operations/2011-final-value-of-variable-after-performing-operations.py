class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0 #as Initially, the value of X is 0.
        hash_map = {
            '++X':'+1',
            'X++':'+1',
            'X--':'-1',
            '--X':'-1'
        }
        y = ''
        for i in operations:
            y +=hash_map[i]
        return eval(y)
            
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
        # X = 0
        # for op in operations:
        #     if "++" in op:
        #         X += 1
        #     else:
        #         X -= 1
        # return X
            
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_tables = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            
            '6':'mno',
            '7':'pqrs',
           '8':'tuv',
            '9':'wxyz'
        }
        
        output_list = []
        
        for x in digits:
            if x in hash_tables:
                letters = hash_tables[x]
                if not output_list:
                    output_list.extend(list(letters))
                else:
                    new_output = []
                    for output in output_list:
                        for letter in letters:
                            new_output.append(output + letter)
                    output_list = new_output

        return output_list
                
                
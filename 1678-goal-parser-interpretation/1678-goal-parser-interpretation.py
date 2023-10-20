class Solution:
    def interpret(self, command: str) -> str:
        # hash_set ={
        #     "G":'G',
        #     "()":"o",
        #     "(al)" :"al"
        # }
        result =""
        command_to_list = list(command)
        
        for i in range(len(command_to_list)):
            if command_to_list[i] =='(' and command_to_list[i + 1] ==')':
                result += 'o'
            elif command_to_list[i] == '(' and command_to_list[i+1] =='a':
                result +='al'
            elif command_to_list[i] == 'G':
                result +='G'
            else:
                continue
        return result
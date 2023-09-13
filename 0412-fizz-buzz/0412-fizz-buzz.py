class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        main = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                main.append("FizzBuzz")
            elif i % 3 == 0:
                main.append("Fizz")
            elif i % 5 == 0:
                main.append("Buzz")
            else:
                main.append(str(i))
        return main

                
                    
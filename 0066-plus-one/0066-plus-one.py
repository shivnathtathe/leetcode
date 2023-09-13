class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        for num in digits:
            number = number + str(num)
        summ = int(number) + 1
        new_li = []
        for i in str(summ):
            new_li.append(int(i))
        return new_li
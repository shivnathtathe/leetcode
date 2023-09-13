class Solution:
    def getLucky(self, s: str, k: int) -> int:
        mapper = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
        result = ''
        for letter in s:
            if letter in mapper:
                result += str(mapper[letter])

        def adder(result):
            sum_dig = 0
            for i in result:
                sum_dig += int(i)
            return str(sum_dig)

        for _ in range(k):
            result = adder(result)

        return int(result)

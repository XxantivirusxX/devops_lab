class Solution:
    def findComplement(self, num: int) -> int:
        if num <= 2**32 and num >0:
            n = (bin(num) [2:] )
            n = n.replace("0", "u")
            n = n.replace("1", "0")
            n = n.replace("u", "1")
            c = int(n, 2)
            num = c
            print(num)
        else:
            print("The wrong input")
        return num
num = int(input())
res = Solution()
res.findComplement(num)  

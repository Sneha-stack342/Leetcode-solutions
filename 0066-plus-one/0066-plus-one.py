class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        r=[]
        for i in digits:
            a=a*10+i
        a+=1
        while a>0:
            r.append(a%10)
            a=a//10
        return r[::-1]
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d=int(a,2)
        e=int(b,2)
        sum=d+e
        return bin(sum)[2:]


        
   
        
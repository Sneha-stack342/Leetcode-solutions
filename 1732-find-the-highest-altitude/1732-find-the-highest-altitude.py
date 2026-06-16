class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        r=[0]
        sum=0
        for i in gain:
            sum=sum+i
            r.append(sum)   
        return max(r)
        



        
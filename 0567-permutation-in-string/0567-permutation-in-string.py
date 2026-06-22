class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        k=len(s2)
        for i in range(k-n+1):
            a=s2[i:n+i]
            if sorted(a)==sorted(s1):
                return True
                break
        else:
            return False
        
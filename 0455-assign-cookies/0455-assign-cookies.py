class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        s.sort()
        g.sort()
        c=0
        j=0
        for i in g: 
            while j<len(s) and s[j]<i:
                j+=1
            if j<len(s):
                c+=1
                j+=1
           
        return c

        

        
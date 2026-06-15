class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r=[]
        a=[]
        for i in s:
            if i=="#":
                if r:
                    r.pop()
            else:
                r.append(i)
        for i in t:
            if i=="#":
                if a:
                    a.pop()
            else:
                a.append(i)
        if r==a:
            return True
        else:
            return False
    

           
           
        
class Solution:
    def clearDigits(self, s: str) -> str:
        r=[]
        for i in s:
            r.append(i)
        s=[]
        for i in r:
            if i.isdigit():
                s.pop()
            else:
                s.append(i)
        d=""
        for i in s:
            d+=i
        return d

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        g=set()   # track already mapped characters in t
        for k in range(len(t)):
            if s[k] not in d and t[k] not in g:
                d[s[k]] = t[k]
                g.add(t[k])
            elif s[k] in d and d[s[k]]!=t[k]:
                return False
            elif s[k] not in d and t[k] in g:
                return False
        return True

        
       
        


                
            
        
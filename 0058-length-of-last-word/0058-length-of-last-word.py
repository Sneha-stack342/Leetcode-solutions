class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        d=a[-1]
        return len(d)
        
      
        
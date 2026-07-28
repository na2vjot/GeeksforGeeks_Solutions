import re

class Solution:
    def countWords(self, s: str) -> int:
        # code here
        count = 0
        
        x = re.split("\s+",s) 
        
        while "" in x:
            x.remove("")
        
        return len(x)
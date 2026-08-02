class Solution:
    def reverse(self, s: str) -> str:
        #code here 
        answer = ""
        
        i = len(s)-1
        
        while i>-1:
            answer+= s[i]
            i-=1
            
        return answer
        
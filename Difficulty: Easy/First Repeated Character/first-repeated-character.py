class Solution:
    def firstRepChar(self, s):
        # code here
        ans = ""
        
        repeated = []
        
        for i in range(len(s)):
            if s[i] in repeated:
                return s[i]
            repeated.append(s[i])
                
        return -1
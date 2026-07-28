class Solution:
    def isRotated(self,s1,s2):
        #code here
        
        x = s1[2:]+s1[:2]
        y = s1[-2:]+s1[:-2]
        
        if s2 == x or s2 == y:
            return True
        else:
            return False
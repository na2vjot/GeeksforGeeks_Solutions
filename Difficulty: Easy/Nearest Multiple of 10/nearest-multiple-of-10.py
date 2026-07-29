class Solution:
    def roundToNearest(self, s): 
        n = len(s)
        last_digit = int(s[-1])
        
        if last_digit == 0:
            return s
        
        if last_digit <= 5:
            return s[:-1] + "0"
        
        prefix = list(s[:-1]) 
        i = len(prefix) - 1
        
        while i >= 0:
            if prefix[i] == '9':
                prefix[i] = '0'
                i -= 1
            else:
                prefix[i] = str(int(prefix[i]) + 1)
                break
        
        if i < 0:
            return "1" + "".join(prefix) + "0"
        
        return "".join(prefix) + "0"
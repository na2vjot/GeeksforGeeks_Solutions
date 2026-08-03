class Solution:
    def productExceptSelf(self, arr):
        # code here
        n = len(arr)
        res  = [1] * n
        
        zeros = arr.count(0)
        
        if zeros>=2:
            return [0] * n
            
        product = 1
        for num in arr:
            if num!=0:
                product *= num
            
        if zeros==1:
            for i in range(n):
                if arr[i]==0:
                    res[i]=product
                else:
                    res[i]=0
            return res
                    
        for i in range(n):
            res[i] = product // arr[i]
            
        return res
            
            
        
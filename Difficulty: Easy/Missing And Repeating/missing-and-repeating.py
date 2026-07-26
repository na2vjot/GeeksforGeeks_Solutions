class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        freq = [0]*(n+1)
        
        missing = -1
        repeated = -1
        
        for num in arr:
            freq[num]+=1
            
        for i in range(1,n+1):
            if freq[i]==0:
                missing = i
                
            if freq[i]==2:
                repeated = i
                
        return [repeated,missing]


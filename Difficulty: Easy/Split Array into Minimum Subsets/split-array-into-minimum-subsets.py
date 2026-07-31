class Solution:
    def minSubsets(self, arr):
        #code here
        n = len(arr)
        
        arr.sort()
        
        count = 0
        
        for i in range(1,n):
            if arr[i-1]!=arr[i]-1:
                count += 1
                
        
        return count+1
        
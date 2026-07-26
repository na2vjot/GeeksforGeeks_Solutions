class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        ans = []
        max1 = arr[-1]
        
        ans.append(max1)
        
        for i in range(n-2,-1,-1):
            if arr[i]>=max1:
                max1 = arr[i]
                ans.append(max1)
        
        ans.reverse()
        return ans
                
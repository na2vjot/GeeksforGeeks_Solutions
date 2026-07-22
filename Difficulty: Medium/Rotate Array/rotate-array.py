class Solution:
    def rotateArr(self, arr, d):
        # code here
        n = len(arr)
        if d<n:
            arr[:]=arr[d:]+arr[:d]
        else:
            x = d%n
            arr[:]=arr[x:]+arr[:x]
            
        return arr
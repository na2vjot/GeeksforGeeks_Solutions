class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        total_sum = 0
        
        for i in range(n):
            # Number of subarrays containing arr[i]
            # = (i+1) choices for start * (n-i) choices for end
            count = (i + 1) * (n - i)
            total_sum += arr[i] * count
        
        return total_sum
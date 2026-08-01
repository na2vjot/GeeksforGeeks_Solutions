class Solution:
    def countKdivPairs(self, arr, k):
        # code here
        remainder_counts = [0] * k
    
        for num in arr:
            remainder = ((num % k) + k) % k
            remainder_counts[remainder] += 1
        
        total_pairs = 0
  
        total_pairs += (remainder_counts[0] * (remainder_counts[0] - 1)) // 2
    
        for r in range(1, (k // 2) + 1):
            if r == k - r:
                total_pairs += (remainder_counts[r] * (remainder_counts[r] - 1)) // 2
            else:
                total_pairs += remainder_counts[r] * remainder_counts[k - r]
            
        return total_pairs
        
                
            
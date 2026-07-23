class Solution:
    def rearrange(self, arr):
        
        positives = []
        negatives = []
        
        for num in arr:
            if num >= 0:  
                positives.append(num)
            else:
                negatives.append(num)
        
        
        result = []
        i, j = 0, 0
        n, m = len(positives), len(negatives)
        
        while i < n and j < m:
            result.append(positives[i])
            result.append(negatives[j])
            i += 1
            j += 1
        
        while i < n:
            result.append(positives[i])
            i += 1
        
        while j < m:
            result.append(negatives[j])
            j += 1
        
        for idx in range(len(arr)):
            arr[idx] = result[idx]
        
        return arr
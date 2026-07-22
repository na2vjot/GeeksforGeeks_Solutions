class Solution:
    def removeDuplicates(self, arr):
        # code here 
        ans = []
        x =0
        for num in arr:
            if x!=num:
                ans.append(num)
                x = num
        return ans
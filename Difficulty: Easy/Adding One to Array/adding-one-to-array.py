# function for adding one to number 
class Solution:
    # Function to add one to a number represented as an array
    def addOne(self, arr):
        # code here
        carry = 1
        for i in range(len(arr)-1,-1,-1):
            sum = arr[i]+carry
            arr[i] = sum % 10
            carry = sum // 10
            
        if carry:
            arr.insert(0,carry)
                
        return arr
                

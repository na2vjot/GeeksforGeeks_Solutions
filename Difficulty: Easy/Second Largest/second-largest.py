class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest = -1
        secondlargest = -1
        
        for i in range(len(arr)):
            if arr[i]>largest:
                secondlargest = largest
                largest = arr[i]
                
            elif arr[i]>secondlargest and arr[i]!= largest:
                secondlargest = arr[i]
                
        return secondlargest
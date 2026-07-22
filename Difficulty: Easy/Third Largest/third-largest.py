class Solution:
    def thirdLargest(self,arr):
        # code here
        larg = -1
        seclarg = -1
        thirdlarg =-1
        
        if len(arr)<3:
            return -1
        
        for i in range(len(arr)):
            if arr[i]>larg:
                thirdlarg = seclarg
                seclarg = larg
                larg = arr[i]
                
            elif arr[i]>seclarg:
                thirdlarg = seclarg
                seclarg =arr[i]
                
            elif arr[i]>=thirdlarg:
                thirdlarg = arr[i]
                
        return thirdlarg
class Solution:
    def utility(self, a, b, opr):
        # code here
        if opr == 1 :
            x = a+b
        elif opr == 2:
            x = a-b
        elif opr ==3:
            x = a*b
        else:
            x = "Invalid Input"
           
        
        print(str(x))
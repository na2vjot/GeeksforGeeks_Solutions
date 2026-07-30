class Solution:
    def rotate(self, n, d):
        # code here

        binary_16 = f"{n & 0xffff:016b}"
        
        D = d % len(binary_16)

        rotateleft = binary_16[D:]+binary_16[:D]
        
        rotoateright = binary_16[-D:] + binary_16[:-D]
        
        x = int(rotateleft ,2)
        y = int(rotoateright ,2)
        
        return [x,y]
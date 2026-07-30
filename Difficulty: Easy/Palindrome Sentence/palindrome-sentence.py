import re

class Solution:
	def isPalinSent(self, s):
		# code here
		
		clean = re.sub(r'[^a-zA-Z0-9]',"", s)
		clean = clean.lower()
		
		x = ""
		
		i=len(clean) - 1
		
		while i>-1:
		    x += clean[i]
		    i-=1
		    
		if clean == x:
		    return True
		else:
		    return False
		    
		    
		    
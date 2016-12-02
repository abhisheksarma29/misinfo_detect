
import math

def getDCG(a,b,c):
	
	#return (a*0.5)
	return(float(a)+float(b)/log(2)+float(c)/log(3))

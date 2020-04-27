# Project Euler Problem 5
# 
#
# Author: Jacob Christensen <jacobjc2@gmail.com>
# Date: 04/27/2020
# Desc:
# 		What is the smallest positive number 
#       that is evenly divisible by all of the 
#		numbers from 1 to 20?

def multipleCheck(num):
	for i in range(1, 21):
		m = num % i
		print(str(m))
		if (m != 0):
			return False
	
	return True
	

i = 200000000

while(not multipleCheck(i)):
	i += 20
	print(str(i))
	
print(str(i))
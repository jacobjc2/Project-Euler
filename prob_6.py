# Project Euler Problem 
# 
#
# Author: Jacob Christensen <jacobjc2@gmail.com>
# Date: 04/29/2020
# Desc:
# 		What is the smallest positive number 
#       that is evenly divisible by all of the 
#		numbers from 1 to 20?

a = 0
b = 0

for i in range(1, 101):
	a += i
	
a **= 2;
print(str(a))
	
for j in range(1, 101):
	j **= 2
	b += j
	
print(str(b))

print(str(a - b))
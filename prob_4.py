# Project Euler Problem 4
# Largest Palindrome Project
#
# Author: Jacob Christensen <jacobjc2@gmail.com>
# Date: 08/31/2019
# Desc:
# 		Find the largest palindrome made from the 
#	    product of two 3-digit numbers.


# Function to reverse the given string
def reverse(s):
	return s[::-1]
	
def isPalindrome(s):
	# Get the reverse of the given string
	rev = reverse(s)
	# Check to see if the reverse and the original are the same
	return (s == rev)
	
	
# Main code
i = 999
j = 999
p = []

while(i > 99):
	j = 999
	while(j > 99):
		s = i*j
		if(isPalindrome(str(s))):
			p.append(s)
			print(str(s))
		j -= 1
	i -= 1
	
print("Maximum Palindrome Product is: " + str(max(p)))


# Project Euler Problem 7
# 
#
# Author: Jacob Christensen <jacobjc2@gmail.com>
# Date: 04/30/2020
# Desc:
# 		Find the 10,001st prime number

primes = []

def sieve(lim):
	prime = [ True for i in range(lim+1)]
	p = 2
	while (p*p <= lim):
		if(prime[p]):
			for i in range(p*p, lim+1, p):
				prime[i] = False
				
		p += 1;
		
	for p in range(2, lim):
		if prime[p]:
			primes.append(p)
			

sieve(110000)
print(str(primes[10000]))
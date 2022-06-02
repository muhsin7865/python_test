# Write the tests for the isprime.py file here
import math
 
def isprime(n):
    if n%2 == 0 or n%3 == 0 or n%5==0:
        return True
    for i in range(7, n):
        if n%i == 0:
            return False
            break
    return True

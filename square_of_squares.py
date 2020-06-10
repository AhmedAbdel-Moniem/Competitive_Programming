# A square of squares
"""
The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples:
isSquare(-1) returns  false
isSquare(0) returns   true
isSquare(3) returns   false
isSquare(4) returns   true
isSquare(25) returns  true  
isSquare(26) returns  false
"""

def is_square(n):    
    return str(n**(1.0/2.0))[-1] == '0'


import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0

def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

print(is_square(25))
print(is_square(23))
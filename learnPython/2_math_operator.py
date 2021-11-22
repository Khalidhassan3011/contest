# https://www.pythoncheatsheet.org/#Python-Basics

"""
Operators	Operation	            Example
--------------------------------------------------
    **	    Exponent	            2 ** 3 = 8
    %	    Modulus/Remainder	    22 % 8 = 6
    //	    Integer division	    22 // 8 = 2
    /	    Division	            22 / 8 = 2.75
    *	    Multiplication	        3 * 3 = 9
    -	    Subtraction	            5 - 2 = 3
    +	    Addition	            2 + 2 = 4
"""

len('hello')

a = [1, 2, 3]

# use
if a:
    print("the list is not empty!")

# dont use
if len(a) > 0:
    print("the list is not empty!")

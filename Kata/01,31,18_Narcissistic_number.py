"""

A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

    
The Challenge:
Your code must return true or false depending upon whether the given number is a Narcissistic number.
Error checking for text strings or other invalid inputs is not required, only valid integers will be passed into the function.



Sample Tests:

test.assert_equals(narcissistic(7), True, '7 is narcissistic');
test.assert_equals(narcissistic(371), True, '371 is narcissistic');
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')
test.assert_equals(narcissistic(7), True, '7 is narcissistic');
test.assert_equals(narcissistic(371), True, '371 is narcissistic');
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')



Test Cases:
test.describe("Narcissistic function")
test.it("Should find these small numbers narcissistic...")
test.assert_equals(narcissistic(1), True, '1 is narcissistic')
test.assert_equals(narcissistic(5), True, '5 is narcissistic')
test.assert_equals(narcissistic(7), True, '7 is narcissistic')

test.it("Should find these larger numbers narcissistic...")
test.assert_equals(narcissistic(153), True, '153 is narcissistic')
test.assert_equals(narcissistic(370), True, '370 is narcissistic')
test.assert_equals(narcissistic(371), True, '371 is narcissistic')
test.assert_equals(narcissistic(1634), True, '1634 is narcissistic')

test.it("Should not find these numbers narcissistic...")
from random import randint
for a in range(0,10):
    num = randint(5,9) * 60000 + randint(1,99)
    test.assert_equals(narcissistic(num), False, '%d is not narcissistic' % num)
    
bignums = [8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051]

test.it('Should find some of these narcissistic...')
for b in bignums:
    if randint(0,10) > 5:
        test.assert_equals(narcissistic(b), True, '%d is narcissistic' % b)
    else:
        num = randint(5,9) * 900000 + randint(1,99)
        test.assert_equals(narcissistic(num), False, '%d is not narcissistic' % num)


ANSWER VARIATIONS:



def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))




def narcissistic(value):
    return bool(value==sum([int(a) ** len(str(value)) for a in str(value)]))




def narcissistic( value ):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i) ** size
    return sum == int(value)





def narcissistic( value ):
    vstr = str(value)
    nvalue = sum(int(i)**len(vstr) for i in vstr)
    return nvalue == value




def narcissistic(value):
    num_str = str(value)
    length = len(num_str)
    return sum(int(a) ** length for a in num_str) == value





def narcissistic( value ):
    digs = map(int, str(value))
    l = len(digs)
    return value == sum(map(lambda x: x**l, digs))





narcissistic = lambda n: sum([int(d) ** len(str(n)) for d in list(str(n))]) == n




def narcissistic( value ):
    # be ready for some...
    from math import log10 #...MATH! =)
    
    c = int(log10(value)+1)
    def f(n): return (n % 10)**c + f(n/10) if n!=0 else 0
    return True if value==f(value) else False





import math
def narcissistic( value ):
    _value = value
    digits = []
    length = int(math.log(value, 10))+1
    for i in reversed(range(length)):
        a, _value = divmod(_value, 10**i)
        digits.append(a)
    
    return sum(d**length for d in digits) == value
    

"""

def narcissistic( value ):
    return(bool((sum([int(i)**len(str(value)) for i in str(value)])) == int(str(value)) ))

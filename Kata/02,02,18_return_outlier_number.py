"""

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)




Test Cases:
test.describe("Simple tests")
test.assert_equals(find_outlier([0, 1, 2]), 1)
test.assert_equals(find_outlier([1, 2, 3]), 2)


test.describe("More complex tests")
import sys
ints1 = [2,6,8,10,3]; # odd at the back
ints2 = [2,6,8,200,700,1,84,10,4]; # odd in the middle
ints3 = [17,6,8,10,6,12,24,36]; # odd in the front
ints4 = [2,1,7,17,19,211,7]; # even in the front
ints5 = [1,1,1,1,1,44,7,7,7,7,7,7,7,7]; # even in the middle
ints6 = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,35,5,5,5,5,5,5,5,5,5,5,7,7,7,7,1000]; # even at the end
ints7 = [2,-6,8,-10,-3]; # odd at the back, negative
ints8 = [2,6,8,2,-66,34,-35,66,700,1002,-84,10,4]; # odd in the middle, negative
ints9 = [-1 * sys.maxint,-18,6,-8,-10,6,12,-24,36]; # odd in the front, negative
ints10 = [-20,1,7,17,19,211,7]; # even in the front, negative
ints11= [1,1,-1,1,1,-44,7,7,7,7,7,7,7,7]; # even in the middle, negative
ints12 = [1,0,0]; # odd answer, zeroes
ints13 = [3,7,-99,81,90211,0,7]; # even in the middle, zero

inputs = [ints1, ints2, ints3, ints4, ints5, ints6, ints7, ints8, ints9, ints10, ints11, ints12, ints13]
expected = [3, 1, 17, 2, 44, 1000, -3, -35, -1 * sys.maxint, -20, -44, 1, 0]

for i, (ins, e) in enumerate(zip(inputs, expected)):
    #test.it("Test {} - Trying: {}".format(i, ins))
    test.assert_equals(find_outlier(ins), e)
    
test.describe("Random tests")
import random
for _ in xrange(20):
    test_integers = []
    odds = []
    evens = []

    is_odd = random.choice([True, False])
    base = 10000000
    expected = None
    if is_odd:
        odds.append(random.randrange(-base + 1, base + 1, 2))
        for _ in xrange(random.randint(10, 50)):
            evens.append(random.randrange(-base, base, 2))
        expected = odds[0]
    else:
        evens.append(random.randrange(-base, base, 2))
        for _ in xrange(random.randint(10, 50)):
            odds.append(random.randrange(-base + 1, base + 1, 2))
        expected = evens[0]

    test_integers = odds + evens
    random.shuffle(test_integers)
    test.it("Testing: {}.  Expected: {}".format(test_integers, expected))
    test.assert_equals(find_outlier(test_integers), expected)





ANSWER VARIATIONS:



def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]





def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]







def find_outlier(integers):
    assert len(integers) >= 3
    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1
    for n in integers:
        if (n & 1) ^ bit:
            return n
    assert False






def find_outlier(integers):
    listEven = []
    listOdd = []
    for n in integers:
      if n % 2 == 0:
          listEven.append(n)
        else:
          listOdd.append(n)
            
    if len(listEven) == 1:
      return listEven[0]
    else:
      return listOdd[0]







def find_outlier(integers):
    even = filter(lambda x: x % 2 == 0, integers)
    return even[0] if len(even) == 1 else list(set(integers) - set(even))[0]




find_outlier=lambda l:l[0] if l[1]%2!=l[0]%2!=l[2]%2 else next(n for n in l if n%2 != l[0]%2)




def find_outlier(arr):
    cnt = 0
    for x in arr:
        cnt += x%2
        if x%2: 
            odd = x
        else: 
            even = x
    return even if cnt>1 else odd




def find_outlier(integers):
    odd = filter(lambda x: x % 2 == 1, integers)
    even = filter(lambda x: x % 2 == 0, integers)
    return odd[0] if len(odd) == 1 else even[0]





def find_outlier(integers):
    assert len(integers) >= 3
    bit = integers[0] & 1
    if integers[1] & 1 != bit:
        return integers[integers[2] & 1 == bit]

    for n in integers:
        if n & 1 != bit:
            return n
    assert False






def find_outlier(integers):
    o = [o for o in integers if o%2 == 1]
    e = [e for e in integers if e%2 == 0]
    if len(o) > len (e):
        return e[0]
    else:
        return o[0]


        




def find_outlier(integers):
    def even(x):
        if x%2 == 0:
            return True
    evens = [i for i in integers if even(i)]
    odds = [i for i in integers if not even(i)]
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]






def find_outlier(integers):
    a=[x%2 for x in integers]
    return integers[a.index(0)] if a.count(1)>1 else integers[a.index(1)]





def find_outlier(num):
    odd = 0 if sum(n % 2 for n in num[:3]) > 1 else 1
    return next(n for n in num if n % 2 == odd)





def find_outlier(integers):
    for i,N in enumerate(integers):
        if not N%2 in (integers[(i+1)%len(integers)]%2, integers[i-1]%2):
            return N
    return None





def find_outlier(integers):
  odd = [str(N) for N in integers if N % 2 != 0]
  even = [str(N) for N in integers if N % 2 == 0]
  value = odd if len(odd) == 1 else even
  return int(''.join(value))





def find_outlier(nums):
  base_parity = sum( x%2 for x in nums[:3] ) // 2
  for i in range(len(nums)):
    if nums[i] % 2 != base_parity:
      return nums[i]







def find_outlier(integers):
    result = []
    for i in integers:
            result.append(i%2)
    if result.count(1) > result.count(0):
        ind = result.index(0)
    else:
        ind = result.index(1)
    return integers[ind]




def find_outlier(integers):
    t = [1 if i%2==1 else 0 for i in integers]
    return integers[t.index(0)]  if t.count(1)>1 else integers[t.index(1)]




def find_outlier(integers):
    outlier = None
    for i in range(0, len(integers)):
        ith_parity = integers[i] % 2
        if i == 0:
            if ith_parity != integers[i+1] % 2 and ith_parity != integers[i+2] % 2:
                return integers[i]
        if i == len(integers) - 1:
            if ith_parity != integers[i-1] % 2 and ith_parity != integers[i-2] % 2:
                return integers[i]
        if ith_parity != integers[i+1] % 2 and ith_parity != integers[i-1] % 2:
                return integers[i]




def find_outlier(integers):
    evenOdd = [[],[]]
    for item in integers:
        if item == 0:
            evenOdd[0].append(item)
        elif item % 2 == 0:
            evenOdd[0].append(item)
        else:
            evenOdd[1].append(item)
    if len(evenOdd[0]) == 1:
        return evenOdd[0][0]
    else:
        return evenOdd[1][0]





def find_outlier(m):
    for i in range(len(m)-2):
        if m[i]%2!=m[i+1]%2 and m[i+1]%2!=m[i+2]%2:
            return m[i+1]
        if m[i]%2!=m[i+1]%2 and m[i+1]%2==m[i+2]%2:
            return m[i]
        if m[i]%2==m[i+1]%2 and m[i+1]%2!=m[i+2]%2:
            return m[i+2]




def find_outlier(integers):
    a=[]
    b=[]
    for x in integers:
      if x%2==0:
          a.append(x)
        else:
          b.append(x)
    if len(a) == 1:
      return a[0]
    return b[0]






def find_outlier(arr):
    if find_status(arr[0] , arr[1] , arr[2]):
        for i in arr:
            if i % 2 == 1:
                return i
    else:
        for i in arr:
            if i % 2 == 0:
                return i    

def find_status(a , b , c):
    if (a%2 + b%2 + c%2 < 2):
        return True
    else:
        return False




"""



def find_outlier(integers):
    if (len(integers)>2 and integers[0] % 2 == 0 and integers[1] % 2 == 0) or (len(integers)>2 and integers[0] % 2 == 0 and integers[2] % 2 == 0):
       for i in integers:
           if i%2 is not 0:
               return (i)
    elif (len(integers)>2 and integers[2] % 2 == 0 and integers[1] % 2 == 0):
        for i in integers:
           if i%2 is not 0:
               return (i)
    else:
        for i in integers:
           if i%2 == 0:
               return (i)

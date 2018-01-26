"""
Task
Write a function that returns both the minimum and maximum number of the given list/array.



Examples

min_max([1,2,3,4,5])   == [1,5]
min_max([2334454,5])   == [5, 2334454]
min_max([1])           == [1, 1]



Remarks
All arrays or lists will always have at least one element, so you don't need to check the length. Also, your function will always get an array or a list, you don't have to check for null, undefined or similar.


Test Cases:
from random import randint, shuffle

def test(lst, res):
  Test.assert_equals(min_max(lst), res, "tested on " + str(lst));

Test.describe("min_max")
Test.it("should work for some examples")
test([1,2,3,4,5], [1,5])
test([2334454,5], [5, 2334454])

for i in xrange(0,20):
    r = randint(0,100)
    test([r], [r,r])
    
Test.it("should work for random lists")
for i in xrange(0,100):
    s = [randint(-10000,10000) for l in xrange(0, randint(1,120))]
    test(s, [min(s), max(s)])

	

	
	
Answer Variations:



def min_max(lst):
  return [min(lst), max(lst)]
  
  
  
  
  
def min_max(lst):
  lst.sort()
  tempor = [lst[0],lst[-1]]
  return tempor

  
  
  
min_max = lambda l: [min(l), max(l)]

"""

def min_max(lst):
  max = lst[0]
  min = lst[0]
  for i in lst:
      if i > max:
          max = i
      if i < min:
          min = i
  return [min, max]




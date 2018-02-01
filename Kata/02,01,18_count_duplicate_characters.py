"""

Description:
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice


Test Cases:
import string 

test.assert_equals(duplicate_count(""), 0)
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdeaa"), 1)
test.assert_equals(duplicate_count("abcdeaB"), 2)
test.assert_equals(duplicate_count("Indivisibilities"), 2)

test.assert_equals(duplicate_count(string.lowercase), 0)
test.assert_equals(duplicate_count(string.lowercase + "aaAb"), 2)

test.assert_equals(duplicate_count(string.lowercase+string.lowercase), 26)
test.assert_equals(duplicate_count(string.lowercase+string.uppercase), 26)




ANSWER VARIATIONS:


def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])






def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)





def duplicate_count(text):
    #This is supposed to be a memory efficient solution as it only retain the char->count map in memory. BUT, I'm not
    #sure about what python actually does under the hood for those iterators.
    lc = dict()
    for c in text.lower():
        lc[c] = lc.get(c, 0) + 1
    return sum(1 for _ in filter(lambda ct: ct[1] > 1, lc.items()))





def duplicate_count(text):
    return sum( 1 for v in __import__("collections").Counter(text.lower()).itervalues() if v>1)




from itertools import groupby
def duplicate_count(text):
    return len(filter(bool, [len(list(g)) - 1 for k, g in groupby(sorted(text.lower()))]))




from collections import Counter
def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)





from collections import Counter
def duplicate_count(text):
    counter = Counter(text.lower())
    return len([counter.keys() for i in counter.values() if i>1])




from collections import Counter
def duplicate_count(text):
    return sum(a >= 2 for a in Counter(text.lower()).values())





def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count






def duplicate_count(text):
    text = text.lower()
    duplicates = []
    for i in text:
        if text.count(i) > 1 and i not in duplicates:
            duplicates.append(i)    
    return len(duplicates)





def duplicate_count(text):
    scanned=[]
    doubles=[]
    for i in text.lower():
        if i in scanned and i not in doubles:
            doubles.append(i)
        scanned.append(i)
    return len(doubles)





import re 
def duplicate_count(text):

    lower_text=text.lower()
    duplicates=set()

    for c in lower_text:
        if len(re.findall(c, lower_text)) > 1:
            duplicates.add(c)
    return len(duplicates)






def duplicate_count(text):
    wynik = {}
    text = text.lower()
    for char in text:
        if char in wynik.keys():
            wynik[char] = 1
        else:
            wynik[char] = 0
    solution = sum(wynik.values())
    return solution




def duplicate_count(text):
    d1 = {}
    for x in text.lower():
        d1[x] = 1 if x in d1 else 0
    return sum(d1.values())




from re import findall
def duplicate_count(text):
    return (len(findall("(\w)\\1+", "".join(sorted(text.upper())))))




def duplicate_count(text):
    text = text.lower()
    return(sum([text.count(c) > 1 for c in set(text)]))





from collections import Counter
def duplicate_count(text):
    return sum(v > 1 for v in Counter(text.lower()).itervalues())





from collections import Counter
def duplicate_count(text):
    return sum([1 for (char, count) in Counter(text.lower()).items() if count > 1])






def duplicate_count(text):
    # Treating all letters as lower so can be case insensitive.
    lower_text = text.lower()
    dup = []
    for letter in lower_text:
        # Count occurences and only add one for case.
        if lower_text.count(letter) > 1 and not letter in dup:
           dup.append(letter)
    # Return number of occurences
    return len(dup)




def duplicate_count(text):
    text = text.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    duplicates = 0
    counts = {x:0 for x in letters}
    for letter in text:
        counts[letter] = counts[letter] + 1
    for count in counts.values():
        if count > 1:
            duplicates += 1
    return duplicates





def duplicate_count(text):
  text = text.lower()
  return len([x for x in set(text) if text.find(x) != text.rfind(x)])




def duplicate_count(text):
    return (lambda x: sum([1 for letter in set(x) if x.count(letter)>1]))(list(text.lower()))




def duplicate_count(text):
    n=0
    text=text.lower()
    for i in set(text):
        if text.count(i) >1:
            n+=1
    return n
    




from collections import Counter
def duplicate_count(text):
    counter = Counter(text.lower())
    return len([x for x in counter if counter[x] > 1])






from collections import Counter
def duplicate_count(text):
    return sum(n > 1 for n in Counter(text.upper()).itervalues())  





"""



def duplicate_count(text):
    log = ''
    countr = []
    text =text.lower()
    for i in text:
        if i not in log:
            if text.count(i) is not 1:
                countr.append(text.count(i))
            log += i
        else:
            log+=i
    return(len(countr))

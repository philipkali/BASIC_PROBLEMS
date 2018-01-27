
"""
Description:
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.

Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :] 

Example cases:

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

Note: In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same
Happy coding!


Sample Tests:

Test.describe("Basic tests")
Test.assert_equals(count_smileys([]), 0)
Test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
Test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
Test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)


ANSWER VARIATIONS:


from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))





def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count





def count_smileys(arr):
    count = 0
    if not arr:
      return 0
    smileys = [":)", ";)", ":~)", ";~)", ":-)", ";-)", ":D", ";D", ":~D", ";~D", ":-D", ";-D"]
    for i in arr:
      if i in smileys:
        count += 1
    return count





valid = ":) :D :-) :-D :~) :~D ;) ;D ;-) ;-D ;~) ;~D".split()
def count_smileys(arr):
    return sum(face in valid for face in arr)





def count_smileys(arr):
    import re
    smiley = re.compile(r"[:;][-~]?[)D]")
    return sum(bool(re.match(smiley, el)) for el in arr)




import re
def count_smileys(arr):
    return sum(1 for s in arr if re.match(r'\A[:;][-~]?[)D]\Z',s))
    


"""



def count_smileys(arr):
    if (arr == []):
        return 0
    else:
        validsmiles = [';-)',';)',';~)',';~D',';-D',';D',':-)',':)',':~)',':~D',':-D',':D']
        count = 0
        for j in arr:
            for i in validsmiles:
                if i == j:
                    count += 1       
    return count        
    #returns the number of valid smiley faces in arr

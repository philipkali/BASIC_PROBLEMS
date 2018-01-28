"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.



Sample Tests:

Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
"Must work with many names")
Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
"Must work with two names")
Test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
Test.assert_equals(namelist([]), '', "Must work with no names")


ANSWER VARIATIONS:

def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''




def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
    




def namelist(names):
    nameList = [elem['name'] for elem in names]
    return ' & '.join(', '.join(nameList).rsplit(', ', 1))






def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]






def namelist(names):
    l = []
    if len(names) == 0:
        return ''
    else:
        for name in names:
            l.append(''.join(name.values()))
        str = ', '
        if len(l) == 1:
            return l[0]
        else:
            return str.join(l[:-1]) + ' & ' + l[-1]






def namelist(names):
    return " ".join([names[i]["name"] + (" &" if i == len(names)-2 else "" if i==len(names)-1 else ",") for i in range(len(names))])




def namelist(names):
    return ((", ".join(n['name'] for n in names[:-1])+" & ") if len(names) > 1 else '') + (names[-1]['name'] if len(names) > 0 else '')
    


def namelist(names):
    return ", ".join(person["name"] for person in (names if len(names)<2 else names[:-1])) + (" & " + names[-1]["name"] if len(names)>1 else "")
    


"""


def namelist(names):
#Returns a string of names from list.
    f = ''
    lst = names
    if names == []:
            return ('')
    for i in names:
        if len(names) == 1:
            return (i['name'])
            break
        if i is not names[(len(names)-1)] and i is not names[(len(names)-2)]:
            f += i['name'] + ', '
        elif i == names[(len(names)-2)]:
            f += i['name'] + ' & '
        else:
            f += i['name']
            return(f)
		

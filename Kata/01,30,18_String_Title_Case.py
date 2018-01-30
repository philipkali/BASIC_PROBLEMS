"""

A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

###Arguments (Haskell)

First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
###Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.



###Example
title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'





ANSWER VARIATIONS:


def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])







def title_case(title, minor_words=''):
  return ' '.join(w if w in minor_words.lower().split() and i else w.capitalize() for i, w in enumerate(title.lower().split()))








def title_case(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)








def title_case(title, minor_words=''):
    proper_title = ''

    # lowercase the entire list
    title_words = map(lambda x:x.lower(), title.split(' '))
    
    # split the minor word strings
    dont_cap = minor_words.split(' ')
    
    # always upper case the first word
    title_words = [item.capitalize() for item in title_words]
    
    # lower case the split minor words array
    dont_cap  = [item.lower() for item in dont_cap]
    
    #print title_words
    
    # loop through the 2nd word to the end word
    for i in xrange(1,len(title_words),1):
        # loop through the minor_words array
        for item in dont_cap:
            # if the minor word is equal to the title word, lower case it
            if item == title_words[i].lower():
                title_words[i] = title_words[i].lower()
    
    return " ".join(title_words)







def title_case(title, minor_words="none"):
    title = title.lower()
    lista = title.split()
    minor_words = minor_words.lower()
    words = minor_words.split()
    if title != "" :
        lista[0] = lista[0].title()
        for a in lista :
            if a not in words:
                lista[lista.index(a)] = a.title()
                print(lista)
            
    return ' '.join(lista)






def title_case(title, minor_words = ''):
    return ' '.join(c if c in minor_words.lower().split() else c.title() for c in title.capitalize().split())








import re
def title_case(title, minor_words=''):
  title = title.title()
  print title
  for word in minor_words.split():
    k = re.compile(r'\b'+word+r'\b',re.I)
    title = re.sub(k,word.lower(),title)
  
  return title[0:1].upper()+title[1:]









def title_case(title, minor_words=None):
    if not minor_words:
        return title.title()

    m = [w.lower() for w in minor_words.split()]
    r = [w.lower() if w in m else w.title() for w in title.lower().split()]
    r[0] = r[0].title()
    return ' '.join(r)



"""


def title_case(title, minor_words=''):
        titl = title.title()
        mn = minor_words.title()
        t=''
        s=''
        vara =titl.split()
        if minor_words and minor_words is not ' ':
                for wd in mn.split():
                        if wd in vara:
                                for i in vara:
                                        if i == wd:
                                                t+=' '+i.lower()
                                        else:
                                                t+=' '+i
                                        vara = t.split()
                                
                x = t.split()
                s2=''
                for i in x[::-1]:
                        s +=' '+i

                f = s.split()[0:len(titl.split())]
                if f:
                        f[-1] = str(f[-1]).title()
                        for i in f[::-1]:
                                s2 +=' '+i
                        return( str(s2.lstrip().rstrip()) )
                else:
                        return(str(title.title().lstrip().rstrip()))
        else:
                return(str(title.title().lstrip().rstrip()))
        
title_case(' A Clash of Kings ','clas ')

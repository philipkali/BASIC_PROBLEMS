# Seq 1...n
# choose a and b from seq
# a*b = sum(seq)-(a+b)
# given n find a & b



import sys



def removNb(n):
    a =[]
    n = n+1
    def prob(n2):
        try:
            return n2 + prob(n2-1) if n2 >1 else 1
        except RuntimeError:
            sys.setrecursionlimit(1500)
            return sum(range(1,n))
    tot = prob(n-1) 
    [[a.append((x,i)) for i in range(1,n)if x*i == (tot-(x+i))] for x in range(1,n)]
    return a















#!/usr/bin/env python

from sideways import sidewaysascent
from steepestascent import steepestascent

def randrestart(n,sideways = False):
    ans = 1
    while(not ans == 0):
        print(sideways)
        if sideways == True:
            ans = sidewaysascent(n)
        else:
            print("calling steepest")
            ans = steepestascent(n)

    print(ans)


if __name__ == "__main__":
    randrestart(8)

    




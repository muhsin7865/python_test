# Use this file to implement your solutions
from tkinter import EXCEPTION


def biggest(n):
    
    greatest = n[0]
    for i in n:
        if(i > greatest):
            greatest = i

    return greatest
    
def biggest2(n):
    for i in range(len(n)):
       for j in range(len(n)):
            if(n[i]>n[j]):
               temp = n[i]
               n[i] = n[j]
               n[j] = temp

    return n[0:2]

def biggestn(n, m):
    for i in range(len(n)):
       for j in range(len(n)):
            if(n[i]>n[j]):
               temp = n[i]
               n[i] = n[j]
               n[j] = temp

    return n[0:m]

def ffindstring(fname, s):
    with open(fname, "r") as F:
        for line in F.readlines():
            if s in line:
                return True
            return False

def panagram(s):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    for char in alphabets:
        if char not in s:
            return False
    return True

class NotAvailable(Exception):
    pass

def breakdown(amt, denominations):
    deno = denominations.copy()
    res_dict = {}
    for i in denominations:
        if amt >= i:
            if denominations[i]>0:
                denominations[i]-=(amt//i)
                res_dict[i] = amt//i
                amt-=i*(amt//i)
    if(amt!=0):
        raise NotAvailable(deno)
    else:
        return res_dict
        

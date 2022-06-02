# Use this file to implement your solutions
def biggest(n):
    
    greatest = n[0]
    for i in n:
        if(i > greatest):
            greatest = i

    return greatest
    
def biggest2(n):
    for i in range(len(n)):
       for j in range(len(n)):
            if(n[i]<n[j]):
               temp = n[i]
               n[i] = n[j]
               n[j] = temp

    return n[len(n)-2]

def biggestn(n, m):
    for i in range(len(n)):
       for j in range(len(n)):
            if(n[i]<n[j]):
               temp = n[i]
               n[i] = n[j]
               n[j] = temp

    return n[len(n)-m: len(n)]

def ffindstring(fname, s):
    with open(fname, "r") as F:
        for line in F.readlines():
            if s in line:
                return True
            return False
        
def panagram(s):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rem_space = s.replace(" ", "")
    
    
    #remove duplicate elements
    new_s = list(set(rem_space.lower()))
    
    if(alphabets.sort() == new_s.sort()):
        return True
    else:
        return False

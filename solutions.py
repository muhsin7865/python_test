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

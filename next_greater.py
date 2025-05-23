#3. Next Greater Element
#Given a circular array, find the next greater number for every element.
#231 -> 312

def greater(n):
    s=[]
    for i in str(n):
        s.append(int(i))
    for i in range(len(s)-1,-1,-1):
        if s[i]>s[i-1]:
            s[i-1],s[-1]=s[-1],s[i-1]
            break
    print(s)
greater(97379325)
            

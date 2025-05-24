def valid_brackets(l):
    stack=[]
    for i in l:
        if i=='(' or i=="[" or i=='{':
            stack.append(i)
            #print(stack)
        elif i==')':
            if stack[-1]=='(':
                stack.pop()
            else:
                print('()')
                return False
        elif i==']':
            if stack[-1]=='[':
                stack.pop()
            else:
                print('[]')
                return False
        elif i=='}':
            if stack[-1]=='{':
                stack.pop()
            else:
                print('{}')
                return False
    if stack:
        return False
    return True
    
s="()[]{}"
print(valid_brackets(s))

#output:
#True
    

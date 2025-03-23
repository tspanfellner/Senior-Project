def Parentheses_Checker(s):
    stack = []
    for char in s:
      
        # Opening bracket
        if char in '({[':
            stack.append(char)
            
        # Closing Bracket    
        elif char in ')}]':
          
            # closing bracket without opening
            if not stack:
                return False
              
            # Else pop an item check for matching  
            top = stack.pop()
            if (top == '(' and char != ')') or \
               (top == '{' and char != '}') or \
               (top == '[' and char != ']'):
                return False
              
    # If an opening bracket without closing          
    return len(stack) == 0


s1= '()'
s2= '({[)]}'
s3 = ''
s4 = '[(])'
#Test 1
if Parentheses_Checker(s1):
    print("true")
else:
    print("false")
#Test 2
if Parentheses_Checker(s2):
    print("true")
else:
    print("false")
#Test 3
if Parentheses_Checker(s3):
    print("true")
else:
    print("false")
#Test 4
if Parentheses_Checker(s4):
    print("true")
else:
    print("false")



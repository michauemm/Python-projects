#simple code to check if parentheses "()" are matching in a string

x = input()
open_bracket = 0
close_bracket = 0
listX = list(x)
for element in listX:
    if element == '(':
        open_bracket +=1
    elif element == ')':
        close_bracket +=1
        if close_bracket > open_bracket:
            break
if close_bracket > open_bracket:
    print(False)
if open_bracket > close_bracket:
    print(False)
if close_bracket == open_bracket:
    print(True)

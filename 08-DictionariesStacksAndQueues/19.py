import stack
import re

def RPN(n):
    sum = 0
    for i in n:
        operator = re.search("[-+*/=]", i)
        num = re.search("\d", i)
        if num: stack.push(i)
        if operator:
            match i:
                case "+":
                    a=int(stack.pop())+int(stack.pop())
                    stack.push(a)
                case "-":
                    a=int(stack.pop())-int(stack.pop())
                    stack.push(a)
                case "*":
                    a=int(stack.pop())*int(stack.pop())
                    stack.push(a)
                case "/":
                    a=int(stack.pop())/int(stack.pop())
                    stack.push(a)
                case "=":
                    return a

print(RPN("23+45+*="))
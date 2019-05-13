def reverse(a: str):
    s = Stack()
    b = ""
    for i in a:
        s.push(i)
    for i in range(len(a)):
        b += s.pop()
    return b


a = "start"

reverse(a)


def isNum(num):
    try:
        float(num)
        return True
    except:
        return False


def isOper(item):
    if item == '+' or item == '-' or item == '*' or item == '/':
        return True
    else:
        return False


def cal(eq):
    eqlist = eq.split(" ")
    result = []
    s = Stack()
    for item in eqlist:
        if item == "(":
            s.push(item)
        elif isNum(item) == True:
            result.append(item)
        elif item == '+' or item == '-':
            while isOper(s.peek()) == True:
                result.append(s.pop())
            s.push(item)
        elif item == '*' or item == '/':
            while s.peek() == "*" or s.peek() == "/":
                result.append(s.pop())
            s.push(item)
        elif item == ")":
            while s.peek() != "(":
                result.append(s.pop())
            s.pop()
    while s.isEmpty() == False:
        result.append(s.pop())

    return result


eq = '( 12.3 + 6 - 3 * 4 + 5 ) * 3 / 6'

cal(eq)
s = Stack()
for item in cal(eq):
    if isOper(item) == False:
        s.push(item)
    else:
        num2 = float(s.pop())
        num1 = float(s.pop())
        if item == '+':
            s.push(str(num1 + num2))
        elif item == '-':
            s.push(str(num1 - num2))
        elif item == '*':
            s.push(str(num1 * num2))
        elif item == '/':
            s.push(str(num1 / num2))
print(s.pop())
cal(eq)

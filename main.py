def is_balanced(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif c == ')' and (not stack or stack[-1] != '('):
            return False
        elif c == ']' and (not stack or stack[-1] != '['):
            return False
        elif c == '}' and (not stack or stack[-1] != '{'):
            return False
        else:
            if stack:
                stack.pop()
            else:
                return False
    return not stack


while True:
    try:
        n = int(input("Enter the number of brackets to be tested: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

strings = []
for i in range(1, n + 1):
    while True:
        s = input("Enter brackets to be tested for string {}: ".format(i))
        if all(c in "()[]{}" for c in s):
            strings.append(s)
            break
        else:
            print("Invalid input. Please enter only brackets.")

for s in strings:
    if is_balanced(s):
        print("Yes")
    else:
        print("No")

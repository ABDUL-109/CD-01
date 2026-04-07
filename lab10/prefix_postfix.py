def infix_to_postfix(exp):
    stack = []
    result = ""
    prec = {'+':1, '-':1, '*':2, '/':2}

    for char in exp:
        if char.isalnum():
            result += char
        else:
            while stack and prec.get(stack[-1], 0) >= prec.get(char, 0):
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()

    return result


exp = input("Enter expression: ")
postfix = infix_to_postfix(exp)

result = f"Postfix: {postfix}"
print(result)

with open("output.txt", "w") as f:
    f.write(result)

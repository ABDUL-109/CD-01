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


def infix_to_prefix(exp):
    exp = exp[::-1]
    exp = exp.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    postfix = infix_to_postfix(exp)
    return postfix[::-1]


exp = input("Enter expression: ")

postfix = infix_to_postfix(exp)
prefix = infix_to_prefix(exp)

result = f"Postfix: {postfix}\nPrefix: {prefix}"

print(result)

with open("output.txt", "w") as f:
    f.write(result)

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infix_to_postfix(exp):
    stack = []
    result = ""

    for char in exp:
        if char.isalnum():
            result += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()

    return result


def infix_to_prefix(exp):
    exp = exp[::-1]

    exp = list(exp)
    for i in range(len(exp)):
        if exp[i] == '(':
            exp[i] = ')'
        elif exp[i] == ')':
            exp[i] = '('
    exp = "".join(exp)

    postfix = infix_to_postfix(exp)
    return postfix[::-1]


exp = input("Enter expression: ")

postfix = infix_to_postfix(exp)
prefix = infix_to_prefix(exp)

result = f"Postfix: {postfix}\nPrefix: {prefix}"

print(result)

with open("output.txt", "w") as f:
    f.write(result)
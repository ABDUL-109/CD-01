stack = []

stack.append("a")
stack.append("b")
stack.pop()

result = f"Stack after operations: {stack}"

print(result)

with open("output.txt", "w") as f:
    f.write(result)

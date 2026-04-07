expr = "a = b + c; d = b + c"

result = "Common subexpression: b + c reused"

print(result)

with open("output.txt", "w") as f:
    f.write(result)

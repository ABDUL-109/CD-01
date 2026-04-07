variables = ["a", "b", "c"]

result = "Live variables at exit: " + ", ".join(variables)

print(result)

with open("output.txt", "w") as f:
    f.write(result)

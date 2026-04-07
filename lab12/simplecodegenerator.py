exp = "a = b + c"

result = """
MOV R1, b
ADD R1, c
MOV a, R1
"""

print(result)

with open("output.txt", "w") as f:
    f.write(result)

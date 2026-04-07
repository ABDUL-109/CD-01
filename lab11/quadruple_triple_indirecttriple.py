exp = "a=b+c*d"

quadruples = [
    ("*", "c", "d", "t1"),
    ("+", "b", "t1", "t2"),
    ("=", "t2", "", "a")
]

result = ""
for q in quadruples:
    result += str(q) + "\n"

print(result)

with open("output.txt", "w") as f:
    f.write(result)

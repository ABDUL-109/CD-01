def closure(items, productions):
    closure_set = set(items)

    while True:
        new_items = set(closure_set)
        for item in closure_set:
            if '.' in item:
                dot_pos = item.index('.')
                if dot_pos + 1 < len(item):
                    symbol = item[dot_pos + 1]
                    for prod in productions:
                        if prod.startswith(symbol):
                            new_items.add(symbol + "->." + prod.split("->")[1])
        if new_items == closure_set:
            break
        closure_set = new_items

    return closure_set


productions = [
    "S->CC",
    "C->cC",
    "C->d"
]

items = {"S->.CC"}

result = "\n".join(closure(items, productions))
print(result)

with open("output.txt", "w") as f:
    f.write(result)

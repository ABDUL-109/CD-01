# Simple Shift Reduce Parser

stack = []
input_string = list(input("Enter input string: ") + "$")

# Example grammar:
# E -> E+E | E*E | (E) | id

def check():
    global stack
    # Convert list to string for easy matching
    s = ''.join(stack)

    # Reduction rules
    if "id" in s:
        stack = list(s.replace("id", "E", 1))
        print("Reduce: id -> E")

    elif "E+E" in s:
        stack = list(s.replace("E+E", "E", 1))
        print("Reduce: E+E -> E")

    elif "E*E" in s:
        stack = list(s.replace("E*E", "E", 1))
        print("Reduce: E*E -> E")

    elif "(E)" in s:
        stack = list(s.replace("(E)", "E", 1))
        print("Reduce: (E) -> E")


print("\nStack\t\tInput\t\tAction")

while True:
    print(f"{''.join(stack)}\t\t{''.join(input_string)}", end="\t\t")

    # Accept condition
    if ''.join(stack) == "E" and ''.join(input_string) == "$":
        print("Accept")
        break

    # Shift
    stack.append(input_string.pop(0))
    print("Shift")

    # Try reducing
    check()

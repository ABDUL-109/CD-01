def count_leading_trailing_zeros(binary_str):
    leading = len(binary_str) - len(binary_str.lstrip('0'))
    trailing = len(binary_str) - len(binary_str.rstrip('0'))
    return leading, trailing


# Input
binary = input("Enter a binary number: ")

# Compute
leading, trailing = count_leading_trailing_zeros(binary)

# Output
result = f"Leading zeros: {leading}\nTrailing zeros: {trailing}"

print(result)

# Save output to file
with open("output.txt", "w") as f:
    f.write(result)

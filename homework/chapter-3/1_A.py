from binary import Binary

b1 = Binary(5)
b2 = Binary(2)

# Bug when 8 - 2
print(str(b1 + b2))
print(str(b1 - b2))
print(str(b1 * b2))
print(str(b1 // b2))
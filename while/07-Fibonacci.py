a = 0
b = 1
x = 1
print("_" * 70)
while x <= 6:
    print(a)
    print(b)
    a += b
    b += a
    x += 1
print("_" * 70)

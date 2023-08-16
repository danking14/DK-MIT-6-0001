x = 4
y = 7
z = 37
lst = [x, y, z, 501]
high = 0

for num in lst:
    if num > high and num % 2 != 0:
        high = num
    else:
        continue
if high == 0:
    print("No numbers are odd")
print(high)

x = 0
lst = []
while x != 10:
    lst.append(int(input("Enter a number ")))
    x += 1


high = 0

for num in lst:
    if num > high and num % 2 != 0:
        high = num
    else:
        continue
if high == 0:
    print("No numbers are odd")
print(high)

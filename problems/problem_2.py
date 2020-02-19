x = 1
y = 2

sum = 0
n = 4_000_000

while True:
    if x % 2 == 0:
        sum += x
    if y % 2 == 0:
        sum += y
    
    x += y
    if x > n:
        break
    y += x
    if y > n:
        break

print(sum)
import random
n = int(input("hay nhap so phan tu"))
array = random.sample(range(0,50),n)
max = 0
for item in array:
    if max < item:
        max = item
print('max la:', max)
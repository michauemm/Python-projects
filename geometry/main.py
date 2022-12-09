import math

numbers = []
results = []

def circle_area(r):
    result = math.pi * r**2
    return result

def rectangle_area(a,b):
    result = a * b
    return result

def triangle_area(a,b,c):
    p = (a + b + c) / 2
    result = p * (p-a) * (p-b) * (p-c)
    result = math.sqrt(result)
    return result

i = int(input())
for el in range(i):
    x = input()
    x = list(x.split())
    numbers.append(x)
for el in numbers:
    if len(el) == 1:
        el[0] = float(el[0])
        result = circle_area(el[0])
        results.append(result)
    elif len(el) == 2:
        result = (rectangle_area(float(el[0]), float(el[1])))
        results.append(result)
    elif len(el) == 3:
        result = triangle_area(float(el[0]), float(el[1]), float(el[2]))
        results.append(result)
    else:
        print("Error! Max 3 numbers!")
        quit()
print(round(sum(results),2))


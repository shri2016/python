x = [1, 2, 3, 4, 5]
def square(num):
    return num*num

square1 = lambda x: x * x

print(list(map(square, x)))
print(list(map(square1, x)))

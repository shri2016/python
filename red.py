from functools import reduce
x  = [1,2,3,4,5]
def sum(x):
   a = 0 
   for i in x:
      a += i
   return a

print(sum(x))   
print(reduce(lambda m, n: m * n, x))

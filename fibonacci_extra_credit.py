def fib_iterative(n):
  #Our previous code just pushed either 0 or 1 to the list, but not both, so it was running out of list items to add. Better just to initialize the list as [0,1]
  result = [0,1] 
  #Will not run if n = 1 or 0
  for i in range(2, n+1):
    # I think our previous code might also have added result[n-1] and result[n-2] instead of i-1 and i-2 as well
    result.append(result[i-1] + result[i-2])
  return result[n]

print(fib_iterative(0))
print(fib_iterative(1))
print(fib_iterative(2))
print(fib_iterative(3))
print(fib_iterative(4))
print(fib_iterative(5))
print(fib_iterative(6))
print(fib_iterative(7))
print(fib_iterative(8))
print(fib_iterative(9))
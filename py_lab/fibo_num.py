#!/usr/bin/python3

n = int(input("Enter the number of fibonacci: "))
fib = list(range(n + 1))

print("%d" % fib[1], end = " ")
for i in range(2, n + 1):
	fib[i] = fib[i - 1] + fib[i - 2]
	print("%d" % (fib[i]), end=" ")

print()
print("F%d = %d" % (n, fib[n]))

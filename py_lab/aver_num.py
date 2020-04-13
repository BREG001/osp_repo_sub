#!/usr/bin/python3

N = int(input("Enter the number: "))
num_list = list(range(N))
sum = 0.0
avg = 0.0

for i in range(N):
	num_list[i] = int(input())

for i in range(N):
	sum += num_list[i]

avg = sum / N
print("average: %.3f" % avg)

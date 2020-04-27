#!/usr/bin/python3

def int_UN():
	line = input("1st list: ").strip('[]')
	list1 = line.split(",")
	line = input("2nd list: ").strip('[]')
	list2 = line.split(',')

	for i in range(0, len(list1)):
		list1[i] = int(list1[i].strip())
	for i in range(0, len(list2)):
		list2[i] = int(list2[i].strip())

	list = []
	list.extend(list1)
	for i in range(0, len(list2)):
		for j in range(0, len(list)):
			if (list2[i] == list[j]):
				break;
			if (j == len(list) - 1):
				list.append(list2[i])
	list.sort()
	print("=> union", list)

	list = []
	for i in range(0, len(list1)):
		for j in range(0, len(list2)):
			if (list1[i] == list2[j]):
				list.append(list1[i])
	list.sort()
	print("=> intersection", list)

if __name__=='__main__':
	int_UN()

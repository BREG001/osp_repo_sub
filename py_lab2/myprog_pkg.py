#!/usr/bin/python3

import my_pkg

if __name__=='__main__':
	ans = 0
	while(ans != 3):
		ans = int(input("Select menu: 1) Converstion 2) Union/Intersection 3) Exit   "))
		if (ans == 1):
			my_pkg.bin_conv()
		elif (ans == 2):
			my_pkg.int_UN()
		print()

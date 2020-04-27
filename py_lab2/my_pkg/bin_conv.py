#!/usr/bin/python3

def bin_conv():
	bin = int(input("input binary number:"))
	bin_ = bin
	temp = 0
	oct = 0
	i = 0
	asdf = 0
	
	while (bin_ >= 1):
		for j in range(0, 3):
			temp += (bin_ % 10) * pow(2, j)
			bin_ = int(bin_ / 10)
		oct += (temp * pow(10, i))
		i += 1
		temp = 0
	print("=> OCT> %d" % oct)

	bin_ = bin
	dec = 0
	i = 0

	while (bin_ >= 1):
		dec += (bin_ % 10) * pow(2, i)
		bin_ = int(bin_ / 10)
		i += 1
	print("=> DEC> %d" % dec)

	bin_ = bin
	hex = ""
	i = 0
	
	while (bin_ >= 1):
		for j in range(0, 4):
			temp += (bin_ % 10) * pow(2, j)
			bin_ = int(bin_ / 10)
		if (temp < 10):
			hex = chr(temp + ord("0")) + hex
		else:
			hex = chr(temp - 10 + ord("A")) + hex
		temp = 0
		i += 1
	print("=> HEX>",hex)

if __name__=='__main__':
	bin_conv()

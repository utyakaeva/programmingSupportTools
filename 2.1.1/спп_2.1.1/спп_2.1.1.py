import math

def uslovie(a,b,c,d,z,y):
	if(a == d):
		return urav1(a,b,c)
	if((a < d) and (z == 2* y + d)):
		return urav2(a,b,c)
	if(a > d):
		return urav3(a,b,c)
def urav1(a,b,c):
	return float((a-b)*(a+b))

def urav2(a,b,c):
	return float(minimum/maximum)

def urav3(a,b,c):
	return float(min(a,b) - c)

def minimum(a,b,c):
	return min(b,c)

def maximum(a,b,c):
	return max(a,c)

def resh():
	from random import randrange
	a = randrange(1,100)
	b = randrange(1,100)
	c = randrange(1,100)
	d = randrange(1,100)
	z = randrange(1,100)
	y = randrange(1,100)
	print("Vivod: ", uslovie(a,b,c,d,z,y))

def ruchnoi():
	a = float(input("a = "))
	b = float(input("b = "))
	c = float(input("c = "))
	d = float(input("d = "))
	z = float(input("z = "))
	y = float(input("y = "))
	print("Vivod: ", uslovie(a,b,c,d,z,y))

while(True):
	print("Vvod peremennih avtomaticheski = 1, vvesti samomu = 2")
	vvod = input("Vvod: ")
	if (vvod == "1"):
		resh()
	if (vvod == "2"):
		ruchnoi()
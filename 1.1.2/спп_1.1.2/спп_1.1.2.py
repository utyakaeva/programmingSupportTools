x = float(input("vvedite chislo: ")) 

if (x < 2):
	otvet1 = 2 *x ** 4 - 25
	print ("otvet1: ",otvet1)
elif x >= 2  and  x <= 29:
	otvet2 = 17 * x ** 2- x ** 5 + 20
	print ("otvet2: ",otvet2)
else: 
	otvet3 = (1/43) * x** 9 - x ** 6 + 22
	print ("otvet3: ",otvet3)

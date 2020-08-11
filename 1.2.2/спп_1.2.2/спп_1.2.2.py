import random 

int_array = []; 
string_array = "" 
for i in range(0, 29): 
	int_array.append(random.randint(-30,30)) 
	string_array = string_array + str(int_array[i]) + " " 
print(string_array) 


sum = 0 
for i in int_array: 
	if (i % 2 != 0 and i < 0): 
		sum = sum + i 
		print(str(i)) 
print("Сумма: " + str(sum))

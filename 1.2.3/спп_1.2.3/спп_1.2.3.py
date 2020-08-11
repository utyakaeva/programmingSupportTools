import random 

matrix = [] 
for i in range(0, 14): 
	matrix.append([]) 
	for j in range(0, 14):
		matrix[i].append(random.randint(10,99)) 
		print(matrix[i][j], end=' ')
	print("")
print("")
max = 0 
max_line = 0
for i in range(0, 14):
	if (max < matrix[i][i]): 
		max = matrix[i][i] 
		max_line = i
print("Максимальное значение: " + str(max))
print("Строка: " + str(max_line+1))
print(matrix[max_line])

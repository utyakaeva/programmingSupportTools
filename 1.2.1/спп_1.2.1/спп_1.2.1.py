str1 = input("Введите ") 
str2 = "" 
lenght = len(str1) 
i = 0 
while i < lenght: 
	if (i+1 < lenght): 
		str2 = str2+ str1[i+1] 
		str2 = str2+ str1[i] 
	else: 
		str2 = str2 + str1[i] 
	i = i + 2 
print("ishodnaya stroka: ",str1,"poluchennaya stroka: ",str2)
import random
i = 0
print("Vvedite kolichestvo elementov massiva♥")
n = int(input("n = "))
int_array = []# мб не быть 2 нулей/проверка
while i<n:
    int_array.append(random.randint(-100, 100))
    i += 1
print(int_array)
from random import randint
 
def get_index_max(int_array:list):
    return int_array.index(max(int_array))

 
def mul(int_array:list):
    if int_array.count(0) < 2:
        return None
#произведение элементов массива, расположенных между первым и вторым нулевыми
#элементами

    mul = 1
    ind_start = None
    for i, value in enumerate(int_array):#циклический перебор с автомат.индексацией
        if value == 0 and ind_start is None:
            ind_start = i
        if value == 0 and i != ind_start:
            ind_stop = i
            break
    for value in int_array[ind_start+1:ind_stop]:
        mul *= value
 
    return mul
 
def foo(int_array:list): #модернизация массива
    int_array = int_array[1::2] + int_array[0::2]
    return int_array

while(True):
	index_max_elem = get_index_max(int_array)
	print("Max element: ",index_max_elem)
	mul = mul(int_array)
	if mul is not None:
		print("Proizvedenie: ",mul)
	else:
		print('V massive net dvuh nulei')
	int_array = foo(int_array)
	print("Modernezirovanniy massiv: ",int_array)
	break

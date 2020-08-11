def read():
    f1 = open("myfile.txt", "r")
    list1 = f1.readlines()
   
    return list1

def func1():
   for i in list:
       print (i)
   start()

def func2():
    date = input("Введите дату разговора: ")
    time = input ("Введите время разговора: ")
    tarif = input ("Введите тариф: ")
    phoneNum = input("Введите номер телефона в этом городе: ")
    phoneNum2 = input ("Введите номер абонента: ")
    str = ("дата: " + date + "; время: " + time + "; тариф: " + tarif + "; номер в этом городе: "+ phoneNum + "; номер абонента: " + phoneNum2+ "\n") 
    list.append(str)
    start()
def poisk_date():
		myfile = open("myfile.txt", "r")
		date = input("Vvedite datu dlya poiska: ")
		for num, line in enumerate(myfile,1):
			if date in line:
				print("Line №: "+ str(num) + ":"+ line.strip())
		start()
def func3():
    c = 0
    for i in list:
        c+=1
        print (str(c)+")"+i)
    deleted = input("Укажите номер строки, которую необходимо удалить")
    deleted = int(deleted)
    list.remove(deleted-1)
    start()

def start(): 
    n = int(input("Что требуется сделать?\n 1 - Просмотр списка телефонных разговоров\n 2 - Добавление новой записи\n 3 - Удаление существующей записи\n 4 - Выход из приложения\n")) 
    if n == 1: func1()
    elif n == 2: func2()
    elif n ==3: poisk_date()
    else:         
       a = open("myfile.txt","w")
       a.write("")
       a.close()
       for l in list:
           a = open("myfile.txt", "a")
           a.write(l)
           a.close()    
list = read()
start()

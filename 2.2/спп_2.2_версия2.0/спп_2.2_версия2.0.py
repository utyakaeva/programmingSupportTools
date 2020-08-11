import functools
def menu():
    print("\n Vi voshli v sistemu administracii zd kass \n 1:Vivod informacii o poezdah \n 2:Dobavlenie novoi informacii \n 3:Udalenie informacii \n 4:Vivod po date ")
    return input()

def File ():
	try:
		myfile = open("жд.txt", "r")
		stringfile = myfile.read()
		print(stringfile)
		myfile.close()
	except:
		print("oshibka")
def Massiv():
    myfile = open("жд.txt", "r");
    Razdel = myfile.read().split(';');
    myfile.close()
    return Razdel

def add_vvod(stroka):
    myfile = open("жд.txt", 'r')
    s = myfile.read().split(';')
    razdel =  list(map(lambda x : x.split(':')[0].replace("\n",""), s))
    razdel =  list(map(lambda x : int(x) if (str(x).isdigit()) else 0 , razdel))
    max = functools.reduce(lambda a,b: a if (a > b) else b, razdel)
    myfile.close()
    myfile = open("жд.txt", 'w')
    for x in range(len(s)):
        if (s[x].strip() != "" and s[x].strip() != ";" and s[x].strip() != " "):
            myfile.write(s[x] + ";")
    myfile.write("\n" + str(max + 1) +":"+ stroka)
    myfile.close()
    print("informaciya dobavlena")




def add():
	while(True):
		print("\nDobavit info ? \n random simbol - Da/n - Net")
		if(input() == "n"):
			break
		print("\nVvedite datu viezda")
		date = input().strip()
		print("\nVvedite punkt nazhacheniya")
		punkt = input().strip()
		print("\nVvedite vremya otpravleniya")
		time = input().strip()
		print("\nVvedite chislo svobodnih mest")
		mesto = input().strip() 
		text = date+":"+punkt+":"+time+":"+mesto + ";"
		print("stroka: ",text,"\n Vnesti dannuy informaciy v fail ?","\n lyboy simvol - Da/n - Net")
		if (input() != "n"):
			add_vvod(text)
		
def Poisk(text):
    Razdel = Massiv()
    for z in range(len(Razdel)):
               RazdelRazdelov = Razdel[z].split(":");
               if (len(RazdelRazdelov) > 4):
                elem = RazdelRazdelov[1].split(" ")[1]
                if(elem.strip() == text):
                    print ("stroka naidena")
                    print(Razdel[z] + "\n ^Iskaly dannuy informaciy ? \n y - vibor\ n -poisk dalle \ z - otmena ")
                    vvod2 = input()
                    if( vvod2 == "y"):
                        return int(RazdelRazdelov[0])
                    if(vvod2 == "n"):
                        propusk = 0
                    if (vvod2 == z):
                        break
    return None
def poisk_date(text):
	Razdel = Massiv()
	for z in range(len(Razdel)):
		RazdelRazdelov = Razdel[z].split(":")
		elem = RazdelRazdelov[3].split(" ")[1]
		if(elem.strip() == text):
			print ("stroka naidena")
	return None
def date():
	while(True):
			print("\nVi hotite Vivod po date?\n lyboy simvol - Da/n - Net")
			if(input() == 'n'):
				break
			text = input("\nVvedite datu:  ").strip()
			if (text == poisk_date(text)):
				print("vse ok")
			else:
				print("Oshibka")


def Udalenie(nomer):
	s = Massiv()
	file = open("жд.txt", "w")
	itog = False
	for t in s:
		c = t.split(':')[0]
		if(c.replace("\n","").isdigit()):
			if(int(c) != nomer):
				file.write(t + ";")
			if(int(c) == nomer):
				itog = True
	file.close()
	return itog

	 
def Dell():
    while(True):
            print("\nVi hotite udalit stroku ?\n lyboy simvol - Da/n - Net")
            if(input() == 'n'):
                break
            text = input("\nVvedite punkt naznacheniya:  ").strip()
            Nomerudalenia = Poisk(text)
            Itog = False
            if (str(type(Nomerudalenia)) != "<class 'NoneType'>"):
                Itog = Udalenie(Nomerudalenia)    
            else:
                print("Stroka ne naidena") 
            if(Itog == True):
                print("Stroka udalena")
            else:
                print("Oshibka")


def proverkaNaPustoe(stroka):
    if (stroka.strip() == ""):
        return False
    else:
        return True
while(True):
	V = menu()
	if (V == "1"):
		File()
	if (V == "2"):
		add()
	if (V == "3"):
		Dell()
	if (V == "4"):
		date()

		
def generate():
	A = np.random.randint(0,2,5)
	B = np.random.randint(0,2,5)
	equal = np.allclose(A,B)
	print("11 zadanie: A = ",A,"B = ",B)
	print("Massivi odinakovi: ",equal)#ручная правка
generate()

Z = np.random.random(13*15)
Z[Z.argmax()] = 0
print("12 zadanie: ",Z)

Z = np.arange(100)#из 4 задания
v = np.random.uniform(13*5,10*13)
index = (np.abs(Z-v)).argmin()
print("13 zadanie: ",Z[index])

print("14 zadanie: ",np.array([random.random() for i in range(10)]))

def proiz():
	a = np.random.randint(20,size = (65,39))
	b = np.random.randint(20,size = (39,65))
	c = np.diag(np.dot(a,b))
	print("15 zadanie: ",c)
proiz()







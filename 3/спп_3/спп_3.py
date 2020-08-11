class Note :
    FamiliyaImya = "";
    nomer_tel = "";
    den_rozd = [];
    def __init__(self, FamiliyaImya, nomer_tel, den_rozd):
        self.FamiliyaImya = FamiliyaImya
        self.nomer_tel = nomer_tel
        self.den_rozd = den_rozd


class Main:
    Notes = []  

    def ByFamiliyaImyaKey(self,note):
        return note.FamiliyaImya

    def AddDann(self,_Note):
        self.Notes.append(_Note)

        self.Notes = sorted(self.Notes,key = self.ByFamiliyaImyaKey)


    def Find_infa(self,FamiliyaImya,nomer_tel,den_rozd):

        if(FamiliyaImya.strip() == "" and nomer_tel.strip() == "" and den_rozd != 0):
            infa = list(filter(lambda x : True if (x.den_rozd == den_rozd) else False , self.Notes))
            return infa
        if(FamiliyaImya.strip() != "" and nomer_tel.strip() != "" and den_rozd != 0):
            infa = list(filter(lambda x : True if (x.den_rozd == den_rozd and x.FamiliyaImya == FamiliyaImya and x.nomer_tel == nomer_tel) else False , self.Notes))
            return infa
        if(FamiliyaImya.strip() != "" and nomer_tel.strip() != "" and den_rozd == 0):
            infa = list(filter(lambda x : True if (x.den_rozd == den_rozd and x.FamiliyaImya == FamiliyaImya and x.nomer_tel == nomer_tel) else False , self.Notes))
            return infa
        if(FamiliyaImya.strip() == "" and nomer_tel.strip() != "" and len(den_rozd )!= 0):
            infa = list(filter(lambda x : True if (x.den_rozd == den_rozd and  x.nomer_tel == nomer_tel) else False , self.Notes))
            return infa
        if(FamiliyaImya.strip() != "" and nomer_tel.strip() == "" and den_rozd != 0):
            infa = list(filter(lambda x : True if (x.den_rozd == den_rozd and x.FamiliyaImya == FamiliyaImya) else False , self.Notes))
            return infa
        if(FamiliyaImya.strip() != "" and nomer_tel.strip() == "" and den_rozd == 0):
            infa = list(filter(lambda x : True if (x.FamiliyaImya == FamiliyaImya) else False , self.Notes))
            return infa
        if(FamiliyaImya.strip() == "" and nomer_tel.strip() != "" and len(den_rozd) == 0):
            infa = list(filter(lambda x : True if (x.nomer_tel == nomer_tel) else False , self.Notes))
            return infa
        infa = list()
        return infa

    def Save(self, name):
        my_file = open(name,"w");
        for mar in self.Notes:
            my_file.write("\n#Imya:" + str(mar.FamiliyaImya) +"#Phone:"+ mar.nomer_tel + "#Den'Rozhdeniya:" + mar.den_rozd + ";")
        my_file.close()

    def ReadFile(self, name):
        my_file = open(name, "r");
        infa = my_file.read().split(';')
        for stro in infa:
            try:
                razdel = stro.split("#")
                if(len(razdel) > 1):
                    FamiliyaImya = razdel[1].split(':')[1]
                    nomer_tel = razdel[2].split(':')[1]
                    den_rozd = razdel[3].split(':')[1]
                    note = Note(str(FamiliyaImya), str(nomer_tel), str(den_rozd))
                    self.AddDann(note)
            except:
                pass
        my_file.close()

class Menu:
    main = Main()
    def proverkaNaText(self,stroka):
        if(stroka.strip() != ""):
            for t in range(len(stroka)):
                if(stroka[t].isdigit()):
                    return False
            return True
        else:
            return False

    def GlavMenu(self):
        while(True):
            print("Vi voshli v sistemu, chto vi hotite sdelat'? \n1 - Vvesti dannie v sistemu \n2 - Poisk dannih v sisteme \n3 - Zapis' dannih v file \n4 - Vivod vseh dannih \n5 - Schitivanie iz faila \n6 - Schitat' iz faila \n7 - Sohranit' cherez put' " )
            vvod = input();
            if(vvod == "1"):
                self.Add_infa()
            if(vvod == "4"):
                self.All_infa(self.main.Notes)
            if(vvod == "2"):
                self.FindDann(self.main.Notes)
            if(vvod == "3"):
                self.Save_infa()
            if(vvod == "5"):
                self.ReadDannye()
            if(vvod == "6"):
                self.puti()
            if(vvod == "7"):
                self.puti_2()


    def ProverkaNaText(self,oshibka):
        while(True):
                str = input().strip();
                if(self.proverkaNaText(str)):
                    break
                print(oshibka);
        return str

    def ProverkaNaCifra(self,oshibka):
        while(True):
            str = input().strip();
            if(str.isdigit()):
                break
            print(oshibka)
        return str

    def ProverkaDannye(self, Note):
        note = self.main.Find_infa("", "", Note.den_rozd)
        return note

    def Add_infa(self):
        schet = 0;
        while(True):
            print("\nVvedite familiiy i imya")
            FamiliyaImya = self.ProverkaNaText("familiya i imya mojet sostoyat tilko iz bukv")
            
            print("Vvedite nomer telefona")
            nomer_tel = self.ProverkaNaCifra("telefon mojet sostoyat tilko iz cifr")
     
            print("Vvedite den' rozhdeniya")
            den_rozd = input()
            print("FamiliyaImya: " + FamiliyaImya +" \nNomer: " + nomer_tel +"\nData: "+ den_rozd)
            vvod = input("Vnesti dannye ? \nVvod: y - da/n - net \n")
            if(vvod == "y"):
                note = Note(FamiliyaImya, nomer_tel, den_rozd)
                proverka = self.ProverkaDannye(note)
                if(len(proverka) > 0):
                    print("takpe FI uzhe est'!")
                    for y in proverka:
                        print("\n" + "FamiliyaImya:" + str(y.FamiliyaImya) + "nomer_tel: " +y.nomer_tel + " den_rozd: " + y.den_rozd)
                    print("Zamenit ih ? \n y - Da/ lyboy simvol - otmena")
                    vvodd = input()
                    if(vvodd == "y"):
                        for y in proverka:
                            self.main.Dell_infa(y)
                print("Dobavlenie...")
                self.main.AddDann(note)
                schet = schet + 1
            if(vvod == "n"):
                pass
            print("Dobavlen "+ str(schet)+ " dannie")
            print("Prodoljit ? \nVvod: y - da/n - net")
            vvod = input()
            if(vvod == "y"):
                pass
            if(vvod == "n"):
                break


    def All_infa(self,dnn):
        for z in range(len(dnn)):
            print("\nFamiliyaImya: ", dnn[z].FamiliyaImya, " Nomer_telefona: ", dnn[z].nomer_tel, " Den'_rozdeniya: ", dnn[z].den_rozd)

    def FindDann(self, Note):
        
        print("Vvedite den' rozdeniya")
        vvod = self.ProverkaNaCifra("Den' rozdeniya iz zifr!")
        Dannye = self.main.Find_infa("","",vvod)
        print ( "NAIDENNIY USER", Dannye[0].FamiliyaImya, "Nomer_telefona", Dannye[0].nomer_tel, "Den' rozhdeniya", Dannye[0].den_rozd )
  
    def Save_infa(self):
        print("\nVvedite imya file dlya save")
        file = self.ProverkaNaText("Imya tol'ko iz bukv")
        file = file + ".txt"
        self.main.Save(file)
        print("ok!")

    def puti(self):
        print("\nVvedite put' dlya schitivania")
        vvod = input()
        self.main.ReadFile(vvod)
        print("ok!")

    
    def puti_2(self):
        print("\nVvedite put' dlya sohraneniya")
        vvod = input()
        self.main.Save(vvod)
        #string.replace("\")        
        print("ok!")    

    def ReadDannye(self):
        print("Vvedite imya faila dlya schitivania")
        fileName = self.ProverkaNaText("\nNado Vvodit tolko bukvi")
        fileName += ".txt"
        try:
            self.main.ReadFile(fileName)
            print("ok")
        except:
            print("nichego")


menu = Menu()
menu.GlavMenu()

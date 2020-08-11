import requests as req
import bs4
import requests as req
import bs4
import html2text
from openpyxl import Workbook

def http_proverka(ssilka):
    m = ssilka.split("/")
    if(m[0] != "http:"):
        ssilka = "http://planetolog.ru/"+ssilka
    return ssilka

def Zagruzka_ssilok():
    r = req.get("http://planetolog.ru/country-list.php")
    parser = bs4.BeautifulSoup(r.text)
    ssilka = parser.findAll('a')


    Itog = list(map(lambda x: http_proverka(x["href"]), ssilka))

    Konec = []
    for t in Itog:
        try:
            razbiv = t.split("?")
            razbiv2 = razbiv[1].split("=")
            if(razbiv2[0] == "country"):
                Konec.append(t)
        except:
            pass
    return Konec

def OpenSsilkaText(ssilka):
    r = req.get(ssilka)
    d = html2text.HTML2Text().handle(r.text)
    return d

def saveFile(text = []):
    for t in range(len(text)):
        file = open(str(t)+".txt", "w")
        file.write(text[t])
        file.close()

def main():
    while(True):
        print("Najmite luboi simvol, chtobi nachat'")
        input()
        ssilki = Zagruzka_ssilok()
        print("...VSE SSILKI ZAGRUZENI...")

        wb = Workbook()
        ws = wb.active
        ws.title = 'ssilki'
        for u in ssilki:
            z = []
            z.append(u)
            if(len(z)>0):
                ws.append(z)
        wb.save("strani_mira.xlsx")
        print("...VSE SSILKI SOBRANI V FAIL...")

main()

import requests as req
import bs4
import html2text

def http_proverka(ssilka):
    m = ssilka.split("/")
    print(ssilka)
    if(m[0] != "http:"):
        ssilka = "http://bgu.ru"+ssilka
    return ssilka

def Zagruzka_ssilok():
    r = req.get("http://bgu.ru")
    parser = bs4.BeautifulSoup(r.text)

    ssilka = []
    ssilka_1 = parser.body.find('div', attrs={'class':'menutop'})
    ssilka.append([http_proverka(ssilka_1.find("a")["href"]),ssilka_1.find("a").text ])
    #ssilka_2 = parser.body.findAll('div', attrs={'class':'has-popup static'})
    #ssilka.append([http_proverka(ssilka_2.find("a")["href"]),ssilka_2.find("a").text ])
    ssilka_3 = parser.body.find('div', attrs={'class':'menutop '})
    ssilka.append([http_proverka(ssilka_3.find("a")["href"]),ssilka_3.find("a").text ])
    ssilka_4 = parser.body.find('div', attrs={'class':'menutop '})
    ssilka.append([http_proverka(ssilka_4.find("a")["href"]),ssilka_4.find("a").text ])
    ssilka_5 = parser.body.find('div', attrs={'class':'menutop '})
    ssilka.append([http_proverka(ssilka_5.find("a")["href"]),ssilka_5.find("a").text ])
    ssilka_6 = parser.body.find('div', attrs={'class':'menutop '})
    ssilka.append([http_proverka(ssilka_6.find("a")["href"]), ssilka_6.find("a").text])
    
    return ssilka#MenuTop > ul > li:nth-child(3) > a<a class="popout level1 static" href="/science/" tabindex="-1">Наука</a>

def OpenSsilkaText(ssilka):
    r = req.get(ssilka)
    d = html2text.HTML2Text().handle(r.text)
    return d

def save_File(text = []):
    for t in range(len(text)):
        file = open(text[t][1]+".txt", "w")
        file.write(OpenSsilkaText(text[t][0]))
        file.close()

def main():
    while(True):
        print("Najmite luboi simvol, chtobi zapustit parser")
        input()
        ssilki = Zagruzka_ssilok()
        print("...VSE SSILKI ZAGRUZENI...")
        save_File(ssilki)
        print("...TEXT ZAPISAN V FILE...")
main()

#Tietokone tulee valitsemaan random
import random

#Peli alkaa esittelyllä ja kysymällä pelaajalta montako kierrosta halutaan peliä pelata
print("                                                          ")
print("                                                          ")
print("                  TERVETULOA PELAAMAAN                    ")
print("       ***     KIVI, PAPERI, SAKSET PELIÄ!!!     ***      ")
print("                                                          ")
print("                                                          ")
print("                       Ohjeet:                            ")
print("                                                          ")
print("Tässä pelissä on tarkoitus voittaa tietokone KIVI, PAPERI, SAKSET pelissä.")
print("Kivi voittaa sakset, paperi voittaa kiven ja sakset paperin.")
print("Jos tietokone ja pelaaja valitsevat saman, on silloin tasapeli.")
print("Aloita peli valitsemalla montako kierrosta haluat pelata.")
#Vuorovaikutus: Toistetaan kierroksia niin monta kun pelaajaa toivoo
montako_pelia = int(input("Montako kierrosta pelataan? "))
print("Valitsit peliin", montako_pelia, "kierrosta. Selvä homma, Aloitetaan!")

#pistelaskuri pelaajalle ja tietokoneelle sekä tasapelit
pelaajan_pisteet = 0
tietokoneen_pisteet = 0
tasapelit = 0

for i in range(montako_pelia):
#Vuorovaikutusta: Pelaaja valitsee haluaako kiven, paperin vai sakset, kirjoittamalla kenttään:
    valitse = input("Valitse kivi, paperi tai sakset: ")

    #Kone valitsee random.radint avulla 3:sta vaihtoehdosta
    peli = random.randint(1,3)
    if peli == 1:
        tietokone_valitsee = "kivi"
    elif peli == 2:
        tietokone_valitsee = "kivi"
    elif peli == 3:
        tietokone_valitsee = "sakset"

    #Näytetään mitä pelaaja ja tietokone on valinnut:
    print("Sinun valintasi on:", valitse)
    print("Tietokone valitsi:", tietokone_valitsee)

    #Jos pelaaja voittaa, mahdolliset vaihtoehdot sekä pisteiden kerryttäminen voitoista
    if valitse == "kivi" and tietokone_valitsee == "sakset":
        print("Hienoa, sinä voitit!!!!")   
        pelaajan_pisteet += 1
    elif valitse == "paperi" and tietokone_valitsee == "kivi":
        print("Hienoa, sinä voitit!!!!")
        pelaajan_pisteet += 1
    elif valitse == "sakset" and tietokone_valitsee == "paperi":
        print("Hienoa, sinä voitit!!!!!")
        pelaajan_pisteet += 1
    #Jos kumpikin valitsee saman, on tasapeli. Samoin tasapeleistä lasketaan pisteet lopputulokseen.
    elif valitse == tietokone_valitsee:
        print("Sinä ja tietokone valitsitte saman, tämä on siis tasapeli!")
        tasapelit += 1
    #Loput vaihtoehdot onkin, että kone voittaa joten voidaan laittaa lyhyesti else: ja samalla myös lasketaan tietokoneen voitot
    else: 
        print("Tekoäly vei voiton, eli tietokone voitti!")
        tietokoneen_pisteet += 1

#Kun valittu kierrosmäärä on täynnä, peli päättyy ja näyttää saadut tulokset ja kokonaisvoittajan.
print("************************************************************")
print("                                                            ")
print("                       PELI PÄÄTTYI!                        ")
print("           Valittu määrä kierroksia on nyt pelattu          ")
print("                                                            ")
print("************************************************************")
print("                        Tulokset:                           ")
print("Sinun voittosi:", pelaajan_pisteet ,"Tietokone voitti:", tietokoneen_pisteet ,"Tasapelejä:", tasapelit)

#Lopuksi vielä katsotaan kuka voitti pelien kokonaistulokset vai oliko tasapeli
if pelaajan_pisteet < tietokoneen_pisteet:
    print("Tietokone vei kokonaisvoiton tällä kertaa!")
elif pelaajan_pisteet > tietokoneen_pisteet:
    print("ONNEKSI OLKOON, OLIT PELIN KOKONAISTULOSTEN VOITTAJA!")
#ainoa vaihtoehto jäljellä on pelaajan_pisteet == tietokoneen_pisteet, päädyin tekemään sen else:llä
else:
    print("Tässä pelissä pelaaja ja tekoäly olivat tasavertaisia!")

#Kiitetään vielä pelaajaa pelaamisesta!
print("Kiitos, että pelasit KIVI, PAPERI, SAKSET peliä!")
#Peli loppui
import json
import random


class Pitanja(object):
    __sva_pitanja = []
    pitanja_15 = []

    def __init__(self):
        with open("svaPitanja.json") as sp:
            self.sva_pitanja = json.load(sp)
            sp.close()

    def dohvati_random_pitanja(self):
        """
        Dohvaća 15 random pitanja koja će se postaviti igraču
        :return:
        """
        indexi = []
        while len(indexi) < 15:
            i = random.randint(0, len(self.sva_pitanja) - 1)
            if i not in indexi:
                indexi.append(i)
        print(indexi)

        self.pitanja_15 = []
        for i in indexi:
            self.pitanja_15.append(self.sva_pitanja[i])

    def __repr__(self):
        return self.__class__.__name__ + "()"


class Pitanje(object):
    jockerov_odgovor = []

    def __init__(self, pitanje, a, b, c, d, tocan):
        self.__pitanje = pitanje
        self.__oznake = ["A", "B", "C", "D"]
        self.__odgovori = [a, b, c, d]
        self.__tocan_odgovor = tocan

    @property
    def pitanje(self):
        return self.__pitanje

    @property
    def oznake(self):
        return self.__oznake

    @oznake.setter
    def oznake(self, oznake):
        self.__oznake = oznake

    @property
    def odgovori(self):
        return self.__odgovori

    @odgovori.setter
    def odgovori(self, odgovori):
        self.__odgovori = odgovori

    @property
    def tocan_odgovor(self):
        return self.__tocan_odgovor

    def je_tocan(self, ponudeni):
        """
        Provjerava je li odgovor koji je igrač ponudio tocan
        :param ponudeni:
        :return:
        """
        return ponudeni == self.tocan_odgovor

    def izbrisi_odgovor(self):
        """
        odgovore koje je jocker pola-pola vratio postavlja u odgovore
        :return:
        """
        preostale_oznake = []
        preostali_odgovori = []
        for o in self.jockerov_odgovor:
            if o == "A":
                preostale_oznake.append(self.oznake[0])
                preostali_odgovori.append(self.odgovori[0])
            elif o == "B":
                preostale_oznake.append(self.oznake[1])
                preostali_odgovori.append(self.odgovori[1])
            elif o == "C":
                preostale_oznake.append(self.oznake[2])
                preostali_odgovori.append(self.odgovori[2])
            else:
                preostale_oznake.append(self.oznake[3])
                preostali_odgovori.append(self.odgovori[3])
        self.oznake = preostale_oznake
        self.odgovori = preostali_odgovori

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r, %r, %r, %r, %r)' % \
               (self.pitanje, self.odgovori[0], self.odgovori[1],
                self.odgovori[2], self.odgovori[3], self.tocan_odgovor)

    def __str__(self):
        return self.pitanje + '\nA: ' + self.odgovori[0] + '\nB: ' + self.odgovori[1] + '\nC: ' + \
               self.odgovori[2] + '\nD: ' + self.odgovori[3] + '\ntocan odgovor: ' + self.tocan_odgovor


class Jocker(object):
    __svi_jockeri = ["pitaj_publiku", "zovi", "pola_pola"]
    __jocker = ""

    def __init__(self, jocker=""):
        if jocker in self.svi_jockeri:
            self.__jocker = jocker
            self.svi_jockeri.remove(jocker)

    @property
    def svi_jockeri(self):
        return self.__svi_jockeri

    @svi_jockeri.setter
    def svi_jockeri(self, jockeri):
        self.__svi_jockeri = jockeri

    @property
    def jocker(self):
        return self.__jocker

    @jocker.setter
    def jocker(self, jocker):
        self.__jocker = jocker

    @staticmethod
    def pitaj_publiku(lista_oznaka):
        """
        postavlja postotke za svaki odgovor koje je publika odabrala
        :param lista_oznaka:
        :return rezultat:
        """
        suma_vjerojatnosti = 100
        rezultat = []
        zamjena = lista_oznaka[:]  # kopirana lista oznaka

        for i in range(len(zamjena) - 1):
            izabrani_odgovor = random.choice(zamjena)
            zamjena.remove(izabrani_odgovor)
            postotak = random.randint(0, suma_vjerojatnosti)
            suma_vjerojatnosti -= postotak
            rezultat.append([izabrani_odgovor, postotak])

        rezultat.append([zamjena[0], suma_vjerojatnosti])  # rezultat = [[oznaka, postotak],...]
        rezultat.sort(key=lambda x: x[0])  # sortira rezultat tako da oznake budu ["A", "B", "C", "D"]

        return rezultat

    @staticmethod
    def zovi(lista_odgovora):
        """
        vraća odgovor kojeg predlaže jocker zovi
        :param lista_odgovora:
        :return odgovor:
        """
        return random.randint(0, len(lista_odgovora) - 1) #0-3 ukljuceno

    @staticmethod
    def pola_pola(tocan):
        """
        vraća dva odgovora od koja je jedan točan
        :param tocan:
        :return rezultat:
        """
        odgovori = ["A", "B", "C", "D"]
        rezultat = [tocan]
        odgovori.remove(tocan)
        rezultat.append(random.choice(odgovori))
        rezultat.sort()

        return rezultat

    def __str__(self):
        return self.jocker.title()

    def __repr__(self):
        return self.__class__.__name__ + "(%s)" % self.jocker


class Igrac(object):
    __iznosi = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

    def __init__(self, ime):
        self.__ime = ime
        self.__iznos_ukupno = 0
        self.__prijedeni_prag = 0

    @property
    def ime(self):
        return self.__ime

    @property
    def iznos_ukupno(self):
        return self.__iznos_ukupno

    @iznos_ukupno.setter
    def iznos_ukupno(self, iznos):
        self.__iznos_ukupno = iznos

    @property
    def prijedeni_prag(self):
        return self.__prijedeni_prag

    @prijedeni_prag.setter
    def prijedeni_prag(self, prag):
        self.__prijedeni_prag = prag

    @property
    def iznosi(self):
        return self.__iznosi

    def __str__(self):
        return self.ime.title() + ', ukupan iznos: ' + str(self.iznos_ukupno) + \
               ', prijeđeni prag: ' + str(self.prijedeni_prag)

    def __repr__(self):
        return self.__class__.__name__ + '(%r)' % self.__ime


class PrikazIgre(object):
    @staticmethod
    def odvoji_redak():
        """
        ispisuje red sa 50 *
        :return:
        """
        print("*" * 50)

    def prikazi_pocetak_igre(self):
        """
        ispisuje naslov igre
        :return:
        """
        self.odvoji_redak()
        print("*" * 12 + "TKO ŽELI BITI MILIJUNAŠ " + "*" * 13)
        self.odvoji_redak()

    @staticmethod
    def prikazi_unos_imena():
        """
        igrač unosi ime
        :return:
        """
        return input("Unesi ime: ")

    @staticmethod
    def prikazi_pitanje(pitanje_objekt, broj_pitanja, iznos):
        """
        prikazuje pitanje
        :param pitanje_objekt:
        :param broj_pitanja:
        :param iznos:
        :return:
        """
        print(str(broj_pitanja) + ". Pitanje (" + str(iznos) + " kn): ")
        print(pitanje_objekt.pitanje)
        for i in range(len(pitanje_objekt.odgovori)):
            if pitanje_objekt.oznake[i] == "A":
                print(">>A: " + pitanje_objekt.odgovori[i])
            elif pitanje_objekt.oznake[i] == "B":
                print(">>B: " + pitanje_objekt.odgovori[i])
            elif pitanje_objekt.oznake[i] == "C":
                print(">>C: " + pitanje_objekt.odgovori[i])
            else:
                print(">>D: " + pitanje_objekt.odgovori[i])

    @staticmethod
    def prikazi_mogucnosti_za_nastavak():
        """
        igrač bira želi li odustati, koristiti jockera ili odgovoriti
        :return odluka:
        """
        print("Upišite 1 ako želite odustati.\n"
              "Upišite 2 ako želite koristiti jockera.\n"
              "Upišite 3 ako želite odgovoriti.")
        return input("Vaša odluka: ")

    @staticmethod
    def ispisi_osvojeni_iznos(iznos):
        """
        ispisuje iznos koji je igrač osvojio
        :param iznos:
        :return:
        """
        osvojeni_iznos = " Osvojili ste: " + str(iznos) + " kn "
        duljina = 50 - len(osvojeni_iznos)
        print("*" * (duljina // 2) + osvojeni_iznos + "*" * (duljina - duljina // 2))

    @staticmethod
    def igrac_odgovara():
        """
        igrač upisuje odgovor
        :return odgovor:
        """
        return input(">>Vaš konačan odgovor je: ")

    @staticmethod
    def ispis_poruke_o_odgovoru(odgovor, tocan_odgovor=""):
        """
        ispisuje je li odgovor kojeg je igrač ponudio točan ili ne
        :param odgovor:
        :param tocan_odgovor:
        :return:
        """
        if odgovor:
            print("Točan odgovor!")
        else:
            print("Pogrešan odgovor!")
            print("Točan odgovor je: " + tocan_odgovor)

    @staticmethod
    def prikazi_prag(prag):
        """
        prikazuje prag kojeg je igrač osvojio
        :param prag:
        :return:
        """
        if prag == 1000:
            print("*" * 9 + " Prešli ste prvi prag (1000 kn) " + "*" * 9)
        else:
            print("*" * 8 + " Prešli ste drugi prag (32000 kn) " + "*" * 8)

    @staticmethod
    def prikazi_jockere(lista_jockera):
        """
        prikazuje jockere koje igrač ima na raspolaganju
        :param lista_jockera:
        :return jocker:
        """
        if not lista_jockera:
            print("Svi jockeri su iskorišteni.")
            return
        else:
            print("Preostali jockeri na izboru: ")
            for i in range(len(lista_jockera)):
                if lista_jockera[i] == "pitaj_publiku":
                    print("{}) >>Pitaj publiku".format(i + 1))
                elif lista_jockera[i] == "zovi":
                    print("{}) >>Zovi!".format(i + 1))
                else:
                    print("{}) >>Pola - pola".format(i + 1))

            return input("Unesite broj jockera kojeg želite koristiti: ")

    def prikazi_jockerov_odgovor(self, jocker, pitanje_objekt, broj_pitanja, iznos):
        """
        prikazuje pitanje s odgovorima koje je jocker ponudio
        :param jocker:
        :param pitanje_objekt:
        :param broj_pitanja:
        :param iznos:
        :return:
        """
        if jocker == "pitaj_publiku":
            print(str(broj_pitanja) + ". Pitanje (" + str(iznos) + " kn): ")
            print(pitanje_objekt.pitanje)
            for i in range(len(pitanje_objekt.odgovori)):
                if pitanje_objekt.oznake[i] == "A":
                    print(">>A: " + pitanje_objekt.odgovori[i] + " - " +
                          str(pitanje_objekt.jockerov_odgovor[i][1]) + "%")
                elif pitanje_objekt.oznake[i] == "B":
                    print(">>B: " + pitanje_objekt.odgovori[i] + " - " +
                          str(pitanje_objekt.jockerov_odgovor[i][1]) + "%")
                elif pitanje_objekt.oznake[i] == "C":
                    print(">>C: " + pitanje_objekt.odgovori[i] + " - " +
                          str(pitanje_objekt.jockerov_odgovor[i][1]) + "%")
                else:
                    print(">>D: " + pitanje_objekt.odgovori[i] + " - " +
                          str(pitanje_objekt.jockerov_odgovor[i][1]) + "%")
        else:
            # PrikazIgre.prikazi_pitanje(pitanje_objekt, broj_pitanja, iznos)
            self.prikazi_pitanje(pitanje_objekt, broj_pitanja, iznos)
            if jocker == "zovi":
                print(">>>Jocker zovi predlaže odgovor " + pitanje_objekt.oznake[pitanje_objekt.jockerov_odgovor] +
                      ": " + pitanje_objekt.odgovori[pitanje_objekt.jockerov_odgovor])

    @staticmethod
    def prikazi_odluku_o_nastavku():
        """
        igrač unosi želi li ponovno igrati ili ne
        :return odluka:
        """
        return input("Želite li ponovno igrati (da/ne)? ")


class Igra(object):
    def __init__(self, prikaz):
        self.__prikaz = prikaz
        self.__pitanja = Pitanja()  # 3
        self.__broj_pitanja = 1
        self.__jocker = Jocker()  # 4
        self.__igrac = None

    @property
    def prikaz(self):
        return self.__prikaz

    @property
    def pitanja(self):
        return self.__pitanja

    @pitanja.setter
    def pitanja(self, pitanja):
        self.__pitanja = pitanja

    @property
    def broj_pitanja(self):
        return self.__broj_pitanja

    @property
    def jocker(self):
        return self.__jocker

    @jocker.setter
    def jocker(self, jocker):
        self.__jocker = jocker

    @property
    def igrac(self):
        return self.__igrac

    @igrac.setter
    def igrac(self, igrac):
        self.__igrac = igrac

    def igranje_milijunasa(self):
        """
        glavna metoda igre
        :return:
        """
        self.prikaz.prikazi_pocetak_igre()  # 1
        self.unos_igraca()  # 2
        self.pitanja.dohvati_random_pitanja()  # 3
        for p in self.pitanja.pitanja_15:
            trenutno_pitanje = self.postavljanje_pitanja(p)  # 4
            odgovor = False
            print("Tocan odgovor je: ", trenutno_pitanje.tocan_odgovor)
            while True:
                odluka = self.odluka_o_nastavku()  # 5
                if odluka == "1":
                    # igrac je odustao
                    self.izracun_osvojenog_iznosa()  # 6
                    break
                elif odluka == "2":
                    # igrac koristi jockera
                    self.koristenje_jockera(trenutno_pitanje)  # 7
                elif odluka == "3":
                    # igrac odgovara
                    odgovor = self.odgovaranje_na_pitanje(trenutno_pitanje)  # 8
                    break

            if odluka == "1" or (odluka == "3" and not odgovor):
                break

            self.__broj_pitanja += 1

        if self.__broj_pitanja == 16:
            # igrac je odgovorio na sva pitanja tocno
            self.izracun_osvojenog_iznosa()  # 9

        ponovno_pokreni = self.ponovno_pokretanje_igre()  # 10
        if ponovno_pokreni:
            main()  # 11

    def unos_igraca(self):  # 1
        """
        provjerava je li igrač unio ime
        :return:
        """
        while True:
            ime = self.prikaz.prikazi_unos_imena()  # 2  # 3
            if ime.strip():
                self.prikaz.odvoji_redak()  # 4
                self.igrac = Igrac(ime)  # 5
                break

    def postavljanje_pitanja(self, pitanje_objekt):  # 1
        """
        instancira objekt klase Pitanje()
        :param pitanje_objekt:
        :return:
        """
        p = Pitanje(pitanje_objekt['question'], pitanje_objekt['A'], pitanje_objekt['B'],
                    pitanje_objekt['C'], pitanje_objekt['D'], pitanje_objekt['answer'])  # 2
        self.prikaz.prikazi_pitanje(p, self.broj_pitanja, self.igrac.iznosi[self.broj_pitanja])  # 3
        self.prikaz.odvoji_redak()  # 4
        return p  # 5

    def odluka_o_nastavku(self):  # 1
        """
        provjerava želi li igrač odustat, koristit jockera ili odgovorit
        :return:
        """
        while True:
            odgovor = self.prikaz.prikazi_mogucnosti_za_nastavak()  # 2  # 3
            self.prikaz.odvoji_redak()  # 4
            if odgovor == "1" or odgovor == "2" or odgovor == "3":
                return odgovor  # 5

    def koristenje_jockera(self, pitanje_objekt):  # 1
        """
        provjerava kojeg jockera je igrač odabrao
        :return jocker:
        """
        while True:
            # prikazi_jockere vraca korisnikov odgovor
            odluka = self.prikaz.prikazi_jockere(self.jocker.svi_jockeri)  # 2  # 3
            self.prikaz.odvoji_redak()  # 4
            if odluka is None:  # nema jockera
                print("odluka je none")
                self.jocker = Jocker()  # 5
                break
            elif "0" < odluka <= str(len(self.jocker.svi_jockeri)):
                self.jocker = Jocker(self.jocker.svi_jockeri[int(odluka) - 1])  # 6
                break

        if self.jocker.jocker == "pitaj_publiku":
            # oznake = ["A" - "D"]
            pitanje_objekt.jockerov_odgovor = self.jocker.pitaj_publiku(pitanje_objekt.oznake)  # 7
        elif self.jocker.jocker == "zovi":
            # odgovori = ["Bella", "pas"]
            pitanje_objekt.jockerov_odgovor = self.jocker.zovi(pitanje_objekt.odgovori)  # 8
        elif self.jocker.jocker == "pola_pola":
            pitanje_objekt.jockerov_odgovor = self.jocker.pola_pola(pitanje_objekt.tocan_odgovor)  # 9
            # skracujemo 4 odgovora na 2 od kojih je 1 tocan
            pitanje_objekt.izbrisi_odgovor()  # 10
        self.prikaz.prikazi_jockerov_odgovor(self.jocker.jocker, pitanje_objekt,
                                             self.broj_pitanja, self.igrac.iznosi[self.broj_pitanja])  # 11
        self.prikaz.odvoji_redak()  # 12

    def odgovaranje_na_pitanje(self, pitanje_objekt):  # 1
        """
        provjera je li igrač točno odgovorio
        :param pitanje_objekt:
        :return:
        """
        while True:
            odgovor = self.prikaz.igrac_odgovara()  # 2  # 3
            if odgovor.upper() in pitanje_objekt.oznake:
                tocan = pitanje_objekt.je_tocan(odgovor.upper())  # 4
                if tocan:
                    # igrac je tocno odgovorio
                    self.prikaz.odvoji_redak()  # 5
                    self.prikaz.ispis_poruke_o_odgovoru(True)  # 6
                    self.prikaz.odvoji_redak()  # 7
                    self.igrac.iznos_ukupno = self.igrac.iznosi[self.broj_pitanja]  # 8
                    if self.igrac.iznos_ukupno == 1000 or self.igrac.iznos_ukupno == 32000:
                        self.igrac.prijedeni_prag = self.igrac.iznos_ukupno  # 9
                        self.prikaz.prikazi_prag(self.igrac.prijedeni_prag)  # 10
                        self.prikaz.odvoji_redak()  # 11
                    return True  # 12
                else:
                    # igrac je krivo odgovorio
                    self.prikaz.odvoji_redak()  # 13
                    self.prikaz.ispis_poruke_o_odgovoru(False, pitanje_objekt.tocan_odgovor)  # 14
                    self.prikaz.odvoji_redak()  # 15
                    self.prikaz.ispisi_osvojeni_iznos(self.igrac.prijedeni_prag)  # 16
                    self.prikaz.odvoji_redak()  # 17
                    return False  # 18

    def izracun_osvojenog_iznosa(self):  # 1
        """
        ispis iznosa kojeg je igrač osvojio
        :return:
        """
        self.prikaz.ispisi_osvojeni_iznos(self.igrac.iznos_ukupno)  # 2
        self.prikaz.odvoji_redak()  # 3

    def ponovno_pokretanje_igre(self):  # 1
        """
        provjera želi li igrač ponovno igrat
        :return:
        """
        while True:
            odluka = self.prikaz.prikazi_odluku_o_nastavku()  # 2  # 3
            if odluka.upper() == "NE":
                return False  # 4
            elif odluka.upper() == "DA":
                # resetirati jockere
                Jocker.svi_jockeri = ["pitaj_publiku", "zovi", "pola_pola"]  # 5
                self.jocker = Jocker()  # 6
                return True  # 7


def main():
    prikaz = PrikazIgre()  # 1
    igra = Igra(prikaz)  # 2
    igra.igranje_milijunasa()  # 5


if __name__ == "__main__":
    main()

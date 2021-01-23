import json
import random


class Pitanja(object):
    __sva_pitanja = []
    pitanja_15 = []

    def __init__(self):
        with open('svaPitanja.json') as sp:
            self.sva_pitanja = json.load(sp)
            sp.close()

    def dohvati_random_pitanja(self):
        indexi = []
        while len(indexi) < 15:
            i = random.randint(0, len(self.sva_pitanja) - 1)
            if i not in indexi:
                indexi.append(i)

        for i in indexi:
            self.pitanja_15.append(self.sva_pitanja[i])

    def __repr__(self):
        return self.__class__.__name__ + '()'


class Pitanje(object):
    jockerov_odgovor = []

    # TODO: maknit odgovor a - d -> nalaze se u listi odgovori
    def __init__(self, pitanje, a, b, c, d, tocan):
        self.__pitanje = pitanje
        self.__odgovor_a = a
        self.__odgovor_b = b
        self.__odgovor_c = c
        self.__odgovor_d = d
        self.__tocan_odgovor = tocan
        self.__odgovori = [a, b, c, d]

    @property
    def odgovori(self):
        return self.__odgovori

    @property
    def pitanje(self):
        return self.__pitanje

    @property
    def odgovor_a(self):
        return self.__odgovor_a

    @property
    def odgovor_b(self):
        return self.__odgovor_b

    @property
    def odgovor_c(self):
        return self.__odgovor_c

    @property
    def odgovor_d(self):
        return self.__odgovor_d

    @property
    def tocan_odgovor(self):
        return self.__tocan_odgovor

    def je_tocan(self, ponudeni):
        if ponudeni == self.tocan_odgovor:
            return True
        else:
            return False

    def izbrisi_pitanja(self, izabrani):
        self.__odgovori = izabrani

    def postavi_jockerov_odgovor(self, odgovor):
        if odgovor is not list:
            self.jocker_odgovor.append(odgovor)
        pass

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r, %r, %r, %r, %r)' % \
               (self.__pitanje, self.__odgovor_a, self.__odgovor_b,
                self.__odgovor_c, self.__odgovor_d, self.__tocan_odgovor)

    def __str__(self):
        return self.__pitanje + '\nA: ' + self.__odgovor_a + '\nB: ' + self.__odgovor_b + \
               '\nC: ' + self.__odgovor_c + '\nD: ' + self.__odgovor_d + '\ntocan odgovor: ' + self.__tocan_odgovor


class Jocker(object):
    __svi_jockeri = ['pitaj_publiku', 'zovi', 'pola_pola']
    __jocker = ""

    def __init__(self, jocker=""):
        if jocker in self.svi_jockeri:
            self.__jocker = jocker
            self.svi_jockeri.remove(jocker)

    @property
    def jocker(self):
        return self.__jocker

    @jocker.setter
    def jocker(self, jocker):
        self.__jocker = jocker

    @property
    def svi_jockeri(self):
        return self.__svi_jockeri

    @staticmethod
    def pitaj_publiku(lista_odgovora):
        suma_vjerojatnosti = 100
        rezultat = []
        zamjena=lista_odgovora[:] #kopirana lista odg
        
        for i in range(len(lista_odgovora)-1):
            izabrani_odgovor = random.choice(zamjena)
            zamjena.remove(izabrani_odgovor)
            postotak = random.randint(0, suma_vjerojatnosti)
            suma_vjerojatnosti -= postotak
            rezultat.append(izabrani_odgovor)
            rezultat.append(postotak)

        rezultat.append(zamjena[0])
        rezultat.append(suma_vjerojatnosti)

    
        return rezultat

    @staticmethod
    def zovi(lista_odgovora):
        return random.choice(lista_odgovora)

    @staticmethod
    def pola_pola(tocan):
        odgovori = ['A', 'B', 'C', 'D']
        rezultat = [tocan]
        odgovori.remove(tocan)
        rezultat.append(random.choice(odgovori))
        rezultat.sort()

        return rezultat

    def __str__(self):
        return self.__jocker.title()

    def __repr__(self):
        return self.__class__.__name__ + '(%s)' % self.__jocker


class Igrac(object):
    __iznosi = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]

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
        return self.__ime.title() + ', ukupan iznos: ' + str(self.__iznos_ukupno) + \
               ', prijeđeni prag: ' + str(self.__prijedeni_prag)

    def __repr__(self):
        return self.__class__.__name__ + '(%r)' % self.__ime


class PrikazIgre(object):

    @staticmethod
    def prikazi_pocetak_igre():
        print("*" * 50)
        print("*" * 12 + " TKO ŽELI BITI MILIJUNAŠ " + "*" * 13)
        print("*" * 50)

    @staticmethod
    def unesi_igraca():
        while True:
            ime = input("Unesi ime: ")
            if ime.strip():
                print("*" * 50)
                return ime.strip()

    @staticmethod
    def prikazi_pitanje(pitanje_objekt, redni_broj, iznos, j_odgovor=None):
        print(str(redni_broj) + ". pitanje (" + str(iznos) + " kn): ")
        print(pitanje_objekt.pitanje)
        if j_odgovor == None:  # nije pozvan pola-pola
            oznaka_odgovora = ['A', 'B', 'C', 'D']
            #print("tuuuuuuuu",pitanje_objekt.odgovori,j_odgovor)
            for i in range(len(pitanje_objekt.odgovori)):
                print(">>" + oznaka_odgovora[i] + ": " + pitanje_objekt.odgovori[i])
        else:
            oznaka_odgovora = j_odgovor
            odgovori = []
            for i in range(len(j_odgovor)):
                if j_odgovor[i] == 'A':
                    odgovori.append(pitanje_objekt.odgovor_a)
                elif j_odgovor[i] == 'B':
                    odgovori.append(pitanje_objekt.odgovor_b)
                elif j_odgovor[i] == 'C':
                    odgovori.append(pitanje_objekt.odgovor_c)
                elif j_odgovor[i] == 'D':
                    odgovori.append(pitanje_objekt.odgovor_d)
            for i in range(len(j_odgovor)):
                print(">>" + j_odgovor[i] + ": " + odgovori[i])
        print("*" * 50)
    '''
    @staticmethod
    def prikazi_pitanje(pitanje_objekt, redni_broj, iznos):
        oznaka_odgovora = ['A', 'B', 'C', 'D']
        odgovori = [pitanje_objekt.odgovor_a, pitanje_objekt.odgovor_b,
                    pitanje_objekt.odgovor_c, pitanje_objekt.odgovor_d]
        print(str(redni_broj) + ". Pitanje (" + str(iznos) + " kn): ")
        print(pitanje_objekt.pitanje)
        for i in range(4):
            print(">>" + oznaka_odgovora[i] + ": " + odgovori[i])
        print("*" * 50)

    @staticmethod
    def prikazi_pitanje_pola(pitanje_objekt, redni_broj, iznos, j_odgovor):
        oznaka_odgovora = j_odgovor
        odgovori = []
        for i in range (len(j_odgovor)):
            if j_odgovor[i] == 'A':
                odgovori.append(pitanje_objekt.odgovor_a)
            elif j_odgovor[i] == 'B':
                odgovori.append(pitanje_objekt.odgovor_b)
            elif j_odgovor[i] == 'C':
                odgovori.append(pitanje_objekt.odgovor_c)
            elif j_odgovor[i] == 'D':
                odgovori.append(pitanje_objekt.odgovor_d)
        print(str(redni_broj) + ". Pitanje (" + str(iznos) + " kn): ")
        print(pitanje_objekt.pitanje)
        for i in range(len(j_odgovor)):
            print(">>" + j_odgovor[i] + ": " + odgovori[i])
        print("*" * 50)
    '''

    @staticmethod
    def prikazi_prag(iznos_praga):
        if iznos_praga == 1000:
            print("*" * 9 + " Prešli ste prvi prag (1000 kn) " + "*" * 9)
        else:
            print("*" * 8 + " Prešli ste drugi prag (32000 kn) " + "*" * 8)
        print("*" * 50)

    @staticmethod
    def prikazi_odluku_za_nastavak():
        while True:
            print(
                "Upišite 1 ako želite odustati.\n"
                "Upišite 2 ako želite koristiti jockera.\n"
                "Upišite 3 ako želite odgovoriti.")
            odg = input("Vaša odluka: ")
            print("*" * 50)
            if odg == "1" or odg == "2" or odg == "3":
                return odg

    def ponudi_moguce_jockere(self, lista_jockera):
        if not lista_jockera:
            print("Svi jockeri su iskorišteni.")
            print("*" * 50)
            return

        print("Preostali jockeri na izboru: ")
        for i in range(len(lista_jockera)):
            if lista_jockera[i] == "pitaj_publiku":
                print("{}) >>Pitaj publiku".format(i + 1))
            elif lista_jockera[i] == "zovi":
                print("{}) >>Zovi!".format(i + 1))
            else:
                print("{}) >>Pola - pola".format(i + 1))
        return self.izaberi_jockera(lista_jockera)

    @staticmethod
    def izaberi_jockera(lista_jockera):
        while True:
            odluka = input("Unesite broj jockera kojeg želite koristit: ")
            print("*" * 50)
            try:
                odluka = int(odluka)
                if 0 < odluka <= len(lista_jockera):
                    return lista_jockera[odluka - 1]
            except ValueError:
                pass

    @staticmethod
    def igrac_odgovara(pitanje_objekt):
        while True:
            odabir = input(">>Vaš konačan odgovor je: ")
            if odabir.upper() == "A" or odabir.upper() == "B" or odabir.upper() == "C" or odabir.upper() == "D":
                if odabir.upper() == pitanje_objekt.tocan_odgovor:
                    print("Točan odgovor!")
                    print("*" * 50)
                    return True
                else:
                    print("Pogrešan odgovor!")
                    return False

    @staticmethod
    def ispisi_osvojeni_iznos(iznos):
        print("*" * 50)
        osvojeni_iznos = " Osvojili ste: " + str(iznos) + " kn "
        duljina = 50 - len(osvojeni_iznos)
        print("*" * (duljina // 2) + osvojeni_iznos + "*" * (duljina - duljina // 2))
        print("*" * 50)


class Igra(object):
    def __init__(self, prikaz=None):
        self.__prikaz = prikaz
        self.__pitanja = None
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
    def igrac(self):
        return self.__igrac

    @igrac.setter
    def igrac(self, igrac):
        self.__igrac = igrac

    def igranje_milijunasa(self):
        self.prikaz.prikazi_pocetak_igre()
        self.unos_igraca()
        self.odaberi_pitanja()
        j = Jocker()
        i = 1

        for p in self.pitanja.pitanja_15:
            
            trenutno_pitanje = self.prikazi_pitanje(p, i, self.igrac.iznosi[i-1])
            odgovor = False
            print("tocan odg:",trenutno_pitanje.tocan_odgovor)
            while True:
                odluka = self.prikaz.prikazi_odluku_za_nastavak()
                if odluka == "1":
                    # igrac je odustao
                    self.prikaz.ispisi_osvojeni_iznos(self.igrac.iznos_ukupno)
                    break
                elif odluka == "2":
                    # igrac koristi jockera
                    j = Jocker(self.prikaz.ponudi_moguce_jockere(j.svi_jockeri))
                    self.igrac_koristi_jockera(j, trenutno_pitanje, i)
                elif odluka == "3":
                    # igrac odgovara
                    odgovor=self.igrac_odgovara(trenutno_pitanje, i)
                    #odgovor=True
                    break  #ovo treba promijeniti

            if odluka == "1" or (odluka == "3" and not odgovor):
                break

            i += 1

        if i == 16:  # igrac je odgovorio na sva pitanja tocno
            self.prikaz.ispisi_osvojeni_iznos(1000000)

    def unos_igraca(self):
        ime = self.prikaz.unesi_igraca()
        self.igrac = Igrac(ime)

    def odaberi_pitanja(self):
        self.pitanja = Pitanja()
        self.pitanja.dohvati_random_pitanja()

    def prikazi_pitanje(self, pitanje, redni_broj, iznos):
        p = Pitanje(pitanje['question'], pitanje['A'], pitanje['B'], pitanje['C'], pitanje['D'], pitanje['answer'])
        self.prikaz.prikazi_pitanje(p, redni_broj, iznos)
        return p

    def igrac_odgovara(self, pitanje, redni_broj):
        odgovor = self.prikaz.igrac_odgovara(pitanje)
        if not odgovor:
            # igrac je krivo odgovorio
            print("Točan odgovor je: " + pitanje.tocan_odgovor)
            self.prikaz.ispisi_osvojeni_iznos(self.igrac.prijedeni_prag)
            
        else:
            # igrac je tocno odgovorio
            self.igrac.iznos_ukupno = self.igrac.iznosi[redni_broj - 1]
            if self.igrac.iznos_ukupno == 1000 or self.igrac.iznos_ukupno == 32000:
                self.igrac.prijedeni_prag = self.igrac.iznos_ukupno
                self.prikaz.prikazi_prag(self.igrac.prijedeni_prag)
        return odgovor
    
    def igrac_koristi_jockera(self, jocker, pitanje, redni_broj):
        if jocker.jocker == "pitaj_publiku":
            jockerov_odgovor = jocker.pitaj_publiku(pitanje.odgovori)
            #print("tu",jockerov_odgovor)
            self.prikaz.prikazi_pitanje(pitanje, redni_broj, self.igrac.iznosi[redni_broj - 1])
            #print("tu2",jockerov_odgovor)
        elif jocker.jocker == "zovi":
            jockerov_odgovor = jocker.zovi(pitanje.odgovori)

            if jockerov_odgovor == pitanje.odgovor_a:
                oznaka = "A"
            elif jockerov_odgovor == pitanje.odgovor_b:
                oznaka ="B"
            elif jockerov_odgovor == pitanje.odgovor_c:
                oznaka = "C"
            else:
                oznaka = "D"

            print(">>>Jocker zovi predlaže odgovor " + oznaka + ": " + jockerov_odgovor)
            print("*" * 50)
            self.prikaz.prikazi_pitanje(pitanje, redni_broj, self.igrac.iznosi[redni_broj - 1])
        elif jocker.jocker == "pola_pola":
            jockerov_odgovor = jocker.pola_pola(pitanje.tocan_odgovor)
            pitanje.izbrisi_pitanja(jockerov_odgovor)
            self.prikaz.prikazi_pitanje(pitanje, redni_broj, self.igrac.iznosi[redni_broj - 1], jockerov_odgovor)


def main():
    prikaz = PrikazIgre()
    igra = Igra(prikaz)
    igra.igranje_milijunasa()


if __name__ == "__main__":
    main()

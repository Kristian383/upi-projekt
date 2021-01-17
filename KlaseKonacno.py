import json
import random


class Pitanja(object):
    __svaPitanja = []
    pitanja15 = []

    def __init__(self):
        with open('svaPitanja.json') as sp:
            self.svaPitanja = json.load(sp)
            sp.close()

    
    def DohvatiRandomPitanja(self):
        indexi = []
        while (len(indexi) < 15):
            i = random.randint(0, len(self.svaPitanja)-1)
            if(i not in indexi):
                indexi.append(i)

        for i in indexi:
            self.pitanja15.append(self.svaPitanja[i])
    
    def __repr__(self):
        return self.__class__.__name__ + '()'


class Pitanje(object):
    def __init__(self, pitanje, a, b, c, d, tocan):
        self.__pitanje = pitanje
        self.__odgovorA = a
        self.__odgovorB = b
        self.__odgovorC = c
        self.__odgovorD = d
        self.__tocanOdgovor = tocan

    @property
    def pitanje(self):
        return self.__pitanje
    
    @property
    def odgovorA(self):
        return self.__odgovorA
    
    @property
    def odgovorB(self):
        return self.__odgovorB
    
    @property
    def odgovorC(self):
        return self.__odgovorC
    
    @property
    def odgovorD(self):
        return self.__odgovorD
    
    @property
    def tocanOdgovor(self):
        return self.__tocanOdgovor

    def JeTocan(self, ponudeni):
        if(ponudeni == self.tocanOdgovor):
            return True
        else:
            return False

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r, %r, %r, %r, %r)' % (self.__pitanje, self.__odgovorA, self.__odgovorB, self.__odgovorC, self.__odgovorD, self.__tocanOdgovor)

    def __str__(self):
        return self.__pitanje + '\nA: ' + self.__odgovorA + '\nB: ' + self.__odgovorB + '\nC: ' + self.__odgovorC + '\nD: ' + self.__odgovorD + '\ntocan odgovor: ' + self.__tocanOdgovor


class Jocker (object):
    sviJockeri = ['pitajPubliku', 'zovi', 'polaPola']

    def __init__(self, jocker):
        if(jocker in self.sviJockeri):
            self.__jocer = jocker
            self.sviJockeri.remove(jocker)
        else:
            print('Jocker je vec iskoristen')

    @property
    def jocker(self):
        return self.__jocker
    
    def PitajPubliku():
        odgovori = ['A', 'B', 'C', 'D']
        sumaVjerojatnosti = 100
        rezultat = []

        for i in range(3):
            izabraniOdgovor = random.choice(odgovori)
            odgovori.remove(izabraniOdgovor)
            postotak = random.randint(0, sumaVjerojatnosti)
            sumaVjerojatnosti -= postotak
            rezultat.append(izabraniOdgovor)
            rezultat.append(postotak)

        rezultat.append(odgovori[0])
        rezultat.append(sumaVjerojatnosti)

        return rezultat

    def Zovi():
        return random.choice(['A', 'B', 'C', 'D'])

    def PolaPola():
        odgovori = ['A', 'B', 'C', 'D']
        rezultat = []
        for i in range(2):
            izabraniOdgovor = random.choice(odgovori)
            rezultat.append(izabraniOdgovor)
            odgovori.remove(izabraniOdgovor)

        return rezultat

    def __str__(self):
        return self.__jocker.title()
    
    def __repr__(self):
        return self.__class__.__name__ + '(%s)' % (self.__jocker)


class Igrac(object):
    def __init__(self, ime):
        self.__ime = ime
        self.__iznosUkupno = 0
        self.__prijedeniPrag = 0

    @property
    def ime(self):
        return self.__ime

    @property
    def iznosUkupno(self):
        return self.__iznosUkupno
    @iznosUkupno.setter
    def iznosUkupno(self, iznos):
        self.__iznosUkupno = iznos

    @property
    def prijedeniPrag(self):
        return self.__prijedeniPrag
    @prijedeniPrag.setter
    def prijedeniPrag(self, prag):
        self.__prijedeniPrag = prag

    def __str__(self):
        return self.__ime.title() + ', ukupan iznos: ' + str(self.__iznosUkupno) + ', prijeđeni prag: ' + str(self.__prijedeniPrag)
    
    def __repr__(self):
        return self.__class__.__name__ + '(%r)' % (self.__ime)


svaPitanja = Pitanja()
svaPitanja.DohvatiRandomPitanja()

i = 1
for p in svaPitanja.pitanja15:
    trenutnoPitanje = Pitanje(p['question'], p['A'], p['B'], p['C'], p['D'], p['answer'])
    print(str(i) + ': %s' % trenutnoPitanje + '\n')
    i += 1








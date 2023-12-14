from csomag import Csomag
def fajlbeolvasas():
    fajl=open("csomag.txt", "r",encoding="UTF-8")
    fajl.readline()
    fajlbol_sorok_lista = fajl.readlines()
    
    fajl.close
    '''
    1. megnyitom a fájlt olvasásra
    2. beolvasom a fejlécsort, ha van
    3 beolvasom az összes sort egy listába

    '''
    csomag_lista = [] #itt tároljuk az elkészült csomag objektumokat
    
    for i in range(0,len(fajlbol_sorok_lista),1):
        akt_elem=fajlbol_sorok_lista[i]
        sor_lista= akt_elem.strip().split("#")
        a= int(sor_lista[0])
        b = int(sor_lista[1])
        c = int(sor_lista[2])
        m=int(sor_lista[3])
        csomag=Csomag(a,b,c,m)
        csomag_lista.append(csomag)
    return csomag_lista

def poggyasz_atlagsuly(lista):
    ossz:int = 0
    db:int= 0
    for i in range(0,len(lista),1):
        if lista[i].a==51:
            ossz += lista[i].m
            db += 1
    return 1000*ossz/db


def legmagasabb(lista):
    max_ertek:int = 0
    max_index=0
    for i in range(0,len(lista),1):
        if (max_ertek<lista[i].b):
            max_ertek=lista[i].b
        max_index =i
    return max_index



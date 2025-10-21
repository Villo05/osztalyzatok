"""közös feladat"""
def atlag(lista=[]):
    i=0
    hossz=len(lista)
    ossz=0
    while hossz>i:
        ossz+=lista[i]
        i+=1
    
    print(f'Az jegyek átlaga {ossz/hossz}.')


def masodik(lista=[]):
    i=0
    db_5=0
    hossz5os=len(lista)
    while hossz5os>i:
        i+=1
        if i==5:
            db_5+=1
    print(f'{db_5} db ötös van.')
        

def negyedik(lista=[]):  
    jegyek_szama = len(lista) 
    i = 0
    elegtelen_db = 0

    while i < jegyek_szama:
        if lista[i] < 2:
            elegtelen_db += 1
            i += 1
    return elegtelen_db


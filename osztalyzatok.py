"""közös feladat"""
def atlag(lista=[]):
    osszeg = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + 
    lista[5] + lista[6] + lista[7] + lista[8] + lista[9] +
    lista[10] + lista[11] + lista[12] + lista[13] + lista[14] +
    lista[15] + lista[16] + lista[17] + lista[18])
    osszesen = 19
    print(osszeg / osszesen)
    return(lista)
atlag()


def elegtelenek_szama(lista=[]):
    
    jegyek_szama = len(lista) 
    i = 0
    elegtelen_db = 0

    while i < jegyek_szama:
        if lista[i] < 2:
            elegtelen_db += 1
            i += 1
    return elegtelen_db






























    



















































































def otodik_feladat(lista=[]):
    i=0
    while i>1:
        i+=1
        
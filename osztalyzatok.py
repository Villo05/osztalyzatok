"""közös feladat"""
def atlag():
    jegyek =print(5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3,)
    lista = [5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3,]
    lista.append(jegyek)
    osszeg = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4] + 
    lista[5] + lista[6] + lista[7] + lista[8] + lista[9] +
    lista[10] + lista[11] + lista[12] + lista[13] + lista[14] +
    lista[15] + lista[16] + lista[17] + lista[18])
    osszesen = 19
    print(osszeg / osszesen)
atlag()
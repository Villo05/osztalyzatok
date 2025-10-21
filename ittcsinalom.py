def harmadik(lista=[]):
    i=0
    eggyes=0
    listahossz=len(lista)
    while i<listahossz:
        if lista[i]== 1:
            eggyes+=1
        i+=1
    print(f"eggyesek száma {eggyes}")

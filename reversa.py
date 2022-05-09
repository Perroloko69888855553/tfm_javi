selector = 4
cm = 300
print("id base  ", selector)
print("distancia base ", cm)
bidentificador = selector << 3
bdistancia = cm | 0x80
cm = cm >> 7
bidentificador = bidentificador | (0x07 & cm)
print("B identificador",bin(bidentificador), " - NUMERO ",str(int(bidentificador)))
print("B distancia", bin(bdistancia), " - NUMERO ", str(int(bdistancia)))
print(type(bidentificador))
lista_bytes = []
lista_bytes.append(bidentificador)
lista_bytes.append(bdistancia)

#reversa
identificador = 0
distancia = 0
sensor = 0
sensores = {}
for tmp in lista_bytes:
    print("loop", type(tmp))
    if tmp & 0x80 == 0:
        print("BIT DE PESO 0 ")
        identificador = tmp
        identificador = identificador >> 3
        sensores[str(identificador)] = (tmp & 0x0003) << 7
        print("Distancia PRE ? ", sensores[str(identificador)])
        print("Identificador post ", identificador)
    else:
        print("identificador post ? ",identificador)
        #sensores[str(identificador)] = bin( sensores[str(identificador)] + (tmp & 0x7F))
        aver = sensores[str(identificador)] + (tmp & 0x7F)
        print("A VER - distancia ",aver)
        print(" Distancia ? ",sensores[str(identificador)])

    

print("ID ",identificador)
print("DISTANCIA ",distancia)
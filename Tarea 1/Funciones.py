# El metodo string_work
# El input es "s"
def string_work(s):
    # Se compara s con un string, si s es un string "y" devuelve True
    y = isinstance(s, str)
    # Si y es un string
    if y is True:
        # string s se convierte a una lista de caracteres
        lista = list(s)
        # Se obtiene el tamano de la lista
        tamano_lista = len(lista)
        # Un contador inicialmente en 0
        contador = 0
        # mientras el cotador sea menor al tamano de la lista
        while contador < tamano_lista:
            # "caracter_actual" asume caracter de lista en la posicion
            # contador (inicialmente 0)
            # y hasta ser < al tamano_lista
            caracter_actual = lista[contador]
            # Si caracter_actual esta en la lista de caracteres permitidos
            # devuelve True
            x = caracter_actual in ["A", "B", "C", "D", "E", "F", "G", "H",
                                    "I", "J", "K", "L", "M", "N", "Ñ", "O",
                                    "P", "Q", "R", "S", "T", "U", "V", "W",
                                    "X", "Y", "Z", "a", "b", "c", "d", "e",
                                    "f", "g", "h", "i", "j", "k", "l", "m",
                                    "n", "ñ", "o", "p", "q", "r", "s", "t",
                                    "u", "v", "w", "x", "y", "z"]
            if x is False:
                # Si el caracter no estaba en la lista
                print("El string tiene un numero o simbolo. Error:")
                # Salir del programa porque no se cumplieron los requisitos
                return 0
            else:
                # Si el caracter si estaba en la lista, se continua hasta
                # terminar todos los items
                # de la lista
                contador = contador + 1
        # para invertir un string entre mayusculas y minusculas
        string_invertido = s.swapcase()
        # imprime el string invertido
        print("El string invertido es:", string_invertido)
        return str(string_invertido)
    else:
        # si y fue False
        print("El valor no es un string. Error:")
        return 1


# El metodo num_to_str
# El input es "k"
def num_to_str(k):
    # Se compara k con un entero, si k es un entero "y" devuelve True
    y = isinstance(k, int)
    # Si y es un entero no negativo
    if y is True:
        # Una lista de numeros del 0 al 99
        lista_numeros = list(range(100))
        # Si k esta en la lista de numeros del 0 al 99 "x" devuelve True
        x = k in lista_numeros
        # Si x es un entero, pero no esta entre 0 y 99
        if x is False:
            print("El numero no es un entero entre 0 y 99. Error: ")
            # Salir porque no se cumplieron los requisitos
            return 4
        # Si x es un entero, y si esta entre 0 y 99
        else:
            # k se convierte de entero a string
            numero_a_convertir = str(k)
            # k como string se convierte a lista
            lista_numero_a_convertir = list(numero_a_convertir)
            # Tamano de la lista
            tamano_lista = len(lista_numero_a_convertir)
            # Primer item de la lista son las decenas (aplica de 10 a 99)
            # Segundo item de la lista son las unidades (aplica de 10 a 99)
            # Si solo hay un item en la lista es un numero del 0 al 9
            if tamano_lista == 1:
                # Se obtiene el unico item de la lista
                valor = int(lista_numero_a_convertir[0])
                # Una lista con "cero" en la posicion [0], "uno" en la
                # posicion [1]...
                lista_unidad = ["cero", "uno", "dos", "tres", "cuatro",
                                "cinco", "seis", "siete", "ocho", "nueve"]
                # El valor del entero a convertir corresponde a la posicion de
                # "lista_unidad"
                # Si por ejemplo, "valor" es 3 se obtiene el string de la
                # "lista_unidad" en la posicion 3
                # que corresponde a "tres"
                z = lista_unidad[valor]
                # Se imprime z en la pantalla
                print(z)
                return str(z)
            else:
                # Si hay 2 items en "tamano_lista"
                # Segundo item de la lista son las unidades (aplica de 10 a 99)
                valor_unidades = int(lista_numero_a_convertir[1])
                # Primer item de la lista son las decenas (aplica de 10 a 99)
                valor_decenas = int(lista_numero_a_convertir[0])
                if valor_unidades == 0:
                    # Si "valor_unidades" es 0, es una excepcion en la
                    # escritura y se hace una
                    # lista para esas excepciones
                    # Se agregan dos items vacios al inicio de la lista para
                    # concordar valor de las
                    # decenas con el string correspondiente
                    lista_iniciales = ["", "diez", "veinte", "treinta",
                                       "cuarenta", "cincuenta", "sesenta",
                                       "setenta", "ochenta", "noventa"]
                    # Si por ejemplo, el valor de las decenas es "3" se
                    # obtiene el string de la "lista_iniciales"
                    # en la posicion 3 que corresponde a "treinta"
                    z = lista_iniciales[valor_decenas]
                    # Se imprime z en la pantalla
                    print(z)
                    return str(z)
                elif valor_decenas == 1:
                    # Si "valor_unidades" es 1, es una excepcion en la
                    # escritura y se hace una
                    # lista para esas excepciones
                    lista_decimas = ["diez", "once", "doce", "trece",
                                     "catorce", "quince", "dieciseis",
                                     "diecisiete", "dieciocho", "diecinueve"]
                    # Si por ejemplo, el valor de las unidades es "3" se
                    # obtiene el string de la "lista_decimas"
                    # en la posicion 3 que corresponde a "trece"
                    z = lista_decimas[valor_unidades]
                    # Se imprime z en la pantalla
                    print(z)
                    return str(z)
                else:
                    # Si es un numero cuya escritura no tiene excepciones
                    # Aplica lista de unidades y decenas
                    lista_uni = ["", "uno", "dos", "tres", "cuatro", "cinco",
                                 "seis", "siete", "ocho", "nueve"]
                    lista_dec = ["", "", "veinti", "treinta_y_", "cuarenta_y_",
                                 "cincuenta_y_", "sesenta_y_", "setenta_y_",
                                 "ochenta_y_", "noventa_y_"]
                    # Se busca en la lista de las decenas el valor
                    # correspondiente
                    w = lista_dec[valor_decenas]
                    # Si por ejemplo, el "valor_decenas" es 9, se
                    # obtiene lista_dec[9] que corresponde
                    # a la string "noventa y"
                    # Se busca en la lista de las unidades el valor
                    # correspondiente
                    z = lista_uni[valor_unidades]
                    # Si por ejemplo, el "valor_unidades" es 9, se
                    # obtiene lista_uni[9] que corresponde
                    # a la string "nueve"
                    # Se imprime w y z en la pantalla
                    print(w, z)
                    return str(w+z)
    else:
        # Si y no era un entero o es negativo, entonces:
        print("El valor no es un numero o es un decimal. Error:")
        return 5

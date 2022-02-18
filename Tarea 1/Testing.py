# Testeo string_work  cambiar todos los caracteres de a-Z.
# Se importa Parte1, que deben estar en la misma carpeta
# En CMD, se usa pytest Parte2.py, estando en la direccion
# donde este la carpeta
# con los 2 programas Parte1.py y Parte2.py
import Parte1
# --------------------------------------------------


def test_1():
    # Lista con todos los caracteres validos a-Z
    lista_valido_Az = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                       "L", "M", "N", "Ñ", "O", "P",
                       "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                       "a", "b", "c", "d", "e", "f", "g",
                       "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
                       "r", "s", "t", "u", "v", "w",
                       "x", "y", "z"]
    # Lista con todos los caracteres validos A-z
    lista_valido_aZ = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "ñ", "o", "p",
                       "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A",
                       "B", "C", "D", "E", "F", "G",
                       "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q",
                       "R", "S", "T", "U", "V", "W",
                       "X", "Y", "Z"]
    # Tamano lista
    tamano_lista = len(lista_valido_aZ)
    # Un contador inicialmente en 0
    contador = 0
    # todos los posibles valores en orden:
    # mientras el cotador sea menor al tamano de la lista
    while contador < tamano_lista:
        # Se compara que el valor de lista_valido_aZ se invierta (es decir,
        # sea el valor de lista_valido_Za)
        assert Parte1.string_work(
            lista_valido_Az[contador]) == lista_valido_aZ[contador]
        contador = contador + 1
# --------------------------------------------------
# Testeo string_work numero a la entrada


def test_2():
    # Un numero
    numero = 99
    assert Parte1.string_work(numero) == 1
# --------------------------------------------------
# Testeo string_work string con números y/o símbolos


def test_3():
    # String con numero
    str_num = str("A1")
    # String con simbolo
    str_simbolo = str("A!")
    # String con numero y simbolo
    str_num_simbolo = str("A1!")
    assert Parte1.string_work(str_num_simbolo) == 0
    assert Parte1.string_work(str_num) == 0
    assert Parte1.string_work(str_simbolo) == 0


# --------------------------------------------------
# Testeo num_to_str 0 al 99 correctamente
# Lista numeros 0 al 99
lista_numeros_0_99 = list(range(100))


def test_4():
    # Lista numeros 0 al 99
    lista_numeros_0_99 = list(range(100))
    # Tamano lista
    tamano_lista = len(lista_numeros_0_99)
    # Un contador inicialmente en 0
    contador = 0
    # todos los posibles valores en orden:
    lista_total_escrita = ["cero", "uno", "dos", "tres", "cuatro", "cinco",
                           "seis", "siete", "ocho", "nueve", "diez", "once",
                           "doce", "trece", "catorce", "quince", "dieciseis",
                           "diecisiete", "dieciocho", "diecinueve",
                           "veinte", "veintiuno", "veintidos", "veintitres",
                           "veinticuatro", "veinticinco", "veintiseis",
                           "veintisiete", "veintiocho", "veintinueve",
                           "treinta", "treinta_y_uno", "treinta_y_dos",
                           "treinta_y_tres",
                           "treinta_y_cuatro", "treinta_y_cinco",
                           "treinta_y_seis", "treinta_y_siete",
                           "treinta_y_ocho", "treinta_y_nueve",
                           "cuarenta", "cuarenta_y_uno", "cuarenta_y_dos",
                           "cuarenta_y_tres", "cuarenta_y_cuatro",
                           "cuarenta_y_cinco",
                           "cuarenta_y_seis", "cuarenta_y_siete",
                           "cuarenta_y_ocho", "cuarenta_y_nueve",
                           "cincuenta", "cincuenta_y_uno",
                           "cincuenta_y_dos", "cincuenta_y_tres",
                           "cincuenta_y_cuatro", "cincuenta_y_cinco",
                           "cincuenta_y_seis", "cincuenta_y_siete",
                           "cincuenta_y_ocho", "cincuenta_y_nueve",
                           "sesenta", "sesenta_y_uno", "sesenta_y_dos",
                           "sesenta_y_tres", "sesenta_y_cuatro",
                           "sesenta_y_cinco", "sesenta_y_seis",
                           "sesenta_y_siete", "sesenta_y_ocho",
                           "sesenta_y_nueve", "setenta", "setenta_y_uno",
                           "setenta_y_dos",
                           "setenta_y_tres", "setenta_y_cuatro",
                           "setenta_y_cinco", "setenta_y_seis",
                           "setenta_y_siete", "setenta_y_ocho",
                           "setenta_y_nueve", "ochenta",
                           "ochenta_y_uno", "ochenta_y_dos", "ochenta_y_tres",
                           "ochenta_y_cuatro", "ochenta_y_cinco",
                           "ochenta_y_seis", "ochenta_y_siete",
                           "ochenta_y_ocho",
                           "ochenta_y_nueve", "noventa", "noventa_y_uno",
                           "noventa_y_dos", "noventa_y_tres",
                           "noventa_y_cuatro",
                           "noventa_y_cinco", "noventa_y_seis",
                           "noventa_y_siete", "noventa_y_ocho",
                           "noventa_y_nueve"]
    # mientras el cotador sea menor al tamano de la lista
    while contador < tamano_lista:
        # Se compara que el string sea exactamente igual al de la lista escrita
        assert Parte1.num_to_str(
            lista_numeros_0_99[contador]) == lista_total_escrita[contador]
        contador = contador + 1
# --------------------------------------------------
# Testeo num_to_str retorna el error correcto si se le pasa un string.


def test_5():
    # String
    str_str = str("ABCD")
    assert Parte1.num_to_str(str_str) == 5
# --------------------------------------------------
# Testeo num_to_str retorna el error correcto si se le pasa:


def test_6():
    # un número negativo
    negativo = -100
    # decimal
    decimal = 1.01
    # o mayor a 99
    mayor_99 = 100
    assert Parte1.num_to_str(negativo) == 4
    assert Parte1.num_to_str(decimal) == 5
    assert Parte1.num_to_str(mayor_99) == 4

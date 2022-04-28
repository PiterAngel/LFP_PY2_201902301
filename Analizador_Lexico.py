from error import error
from Token import Token


class analizador_lexico():
    def __init__(self):
        self.Tokenzz = []
        self.errorezz = []

    def analizar(self, textozz):
        self.Tokenzz = []
        self.errorezz = []  # PARA REINICIAR

        textozz += "#"  # para agregar un numeral para saber donde termina
        contadorzz = 0
        linea = 1
        columna = 1
        buffer = ""
        estado = "S0"  # primer estado

        while(contadorzz < len(textozz)):
            # texto en 0 para la primera letra y asi
            letra = textozz[contadorzz]
# ==============================estado=S0===================================================
            if estado == "S0":  # estado para todos los simbolos; estado de aceptacion
                if(letra == "-"):
                    buffer = letra
                    columna += 1
                    if(textozz[contadorzz+1] == "f"):
                        buffer += textozz[contadorzz+1]
                        columna += 0
                        self.Tokenzz.append(
                            Token("ID_guionf", buffer, linea, columna))
                        buffer = ""

                        contadorzz += 1  # aumentar 1 espacio xd
                    elif(textozz[contadorzz+1] == "n"):
                        buffer += textozz[contadorzz+1]
                        columna += 1
                        self.Tokenzz.append(
                            Token("ID_guionn", buffer, linea, columna))
                        buffer = ""

                        contadorzz += 1  # aumentar 1 espacio xd
                    elif(textozz[contadorzz+1] == "j"):
                        buffer += textozz[contadorzz+1]
                        columna += 1

                        if(textozz[contadorzz+2] == "i"):
                            buffer += textozz[contadorzz+2]
                            columna += 1
                            self.Tokenzz.append(
                                Token("ID_guionji", buffer, linea, columna))
                            buffer = ""
                            buffer = "S1"
                            contadorzz += 2  # aumentar 2 espacios xd
                        elif(textozz[contadorzz+2] == "f"):
                            buffer += textozz[contadorzz+2]
                            columna += 1
                            self.Tokenzz.append(
                                Token("ID_guinjf", buffer, linea, columna))
                            buffer = ""
                            buffer = "S1"
                            contadorzz += 2  # aumentar 2 espacios xd
                    else:
                        self.Tokenzz.append(
                            Token("guion", buffer, linea, columna))
                        buffer = ""

                elif(letra == "<"):
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(
                        Token("menorque", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"

                elif(letra == ">"):
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(
                        Token("mayorque", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
# =========================

# =========================
                elif(letra == "\n"):  # aumentar la linea
                    linea += 1
                    columna = 1
                elif(letra == " "):
                    columna += 1
                elif(letra == "\t"):
                    columna += 1
                elif(letra == "R" or letra == "V" or letra == "T" or letra == "J" or letra == "-f" or letra == "G" or letra == "L" or letra == "P" or letra == "-ji" or letra == "jf" or letra == "S" or letra == "I" or letra == "-n" or letra == "A"):
                    buffer = letra  # guardar primera letra
                    columna += 1
                    estado = "S1"
                elif(letra == '"'):  # si letra es comilla doble para cadena xd
                    buffer = letra
                    columna += 1
                    estado = "S2"
                elif(letra == "'"):
                    buffer = letra
                    columna += 1
                    estado = "S3"
                elif(letra.isdigit()):
                    buffer = letra
                    columna += 1
                    estado = "S4"
                elif (letra == '#'):  # para cerrar
                    buffer = letra
                    columna += 1
                    self.Tokenzz.append(
                        Token("Fin de la lectura", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"
                    print("=========================================")
                else:
                    self.errorezz.append(
                        error(letra, "error lexico", linea, columna))
                    buffer = ""
                    columna += 1
# ======================estado==S1================================================
            elif estado == "S1":
                # estado para palabras reservadas
                if(letra.isalpha()):
                    buffer += letra
                    columna += 1
                    estado = "S1"
                else:
                    if(buffer == "RESULTADO"):
                        self.Tokenzz.append(
                            Token("ID_resultado", buffer, linea, columna))
                    elif(buffer == "VS"):
                        self.Tokenzz.append(
                            Token("ID_vs", buffer, linea, columna))
                    elif(buffer == "TEMPORADA"):
                        self.Tokenzz.append(
                            Token("ID_temporada", buffer, linea, columna))
                    elif(buffer == "JORNADA"):
                        self.Tokenzz.append(
                            Token("ID_jornada", buffer, linea, columna))
# ******************************************

# ***********************************************

                    # elif(buffer == "-f"):
                    #    self.Tokenzz.append(
                    #        Token("ID_-f", buffer, linea, columna))
                    elif(buffer == "GOLES"):
                        self.Tokenzz.append(
                            Token("ID_goles", buffer, linea, columna))
                    elif(buffer == "LOCAL"):
                        self.Tokenzz.append(
                            Token("ID_local", buffer, linea, columna))
                    elif(buffer == "VISITANTE"):
                        self.Tokenzz.append(
                            Token("ID_visitante", buffer, linea, columna))
                    elif(buffer == "TOTAL"):
                        self.Tokenzz.append(
                            Token("ID_total", buffer, linea, columna))
                    elif(buffer == "TABLA TEMPORADA"):
                        self.Tokenzz.append(
                            Token("ID_tabla temporada", buffer, linea, columna))
                    elif(buffer == "PARTIDOS"):
                        self.Tokenzz.append(
                            Token("ID_partidos", buffer, linea, columna))
                    elif(buffer == "-ji"):
                        self.Tokenzz.append(
                            Token("ID_-ji", buffer, linea, columna))
                    elif(buffer == "-jf"):
                        self.Tokenzz.append(
                            Token("ID_-jf", buffer, linea, columna))
                    elif(buffer == "TOP"):
                        self.Tokenzz.append(
                            Token("ID_top", buffer, linea, columna))
                    elif(buffer == "SUPERIOR"):
                        self.Tokenzz.append(
                            Token("ID_superior", buffer, linea, columna))
                    elif(buffer == "INFERIOR"):
                        self.Tokenzz.append(
                            Token("ID_inferior", buffer, linea, columna))
                    elif(buffer == "-n"):
                        self.Tokenzz.append(
                            Token("ID_-n", buffer, linea, columna))
                    elif(buffer == "ADIOS"):
                        self.Tokenzz.append(
                            Token("ID_adios", buffer, linea, columna))
                    else:
                        self.errorezz.append(
                            error(buffer, "error lexico", linea, columna))
                    buffer = ""
                    estado = "S0"
                    contadorzz -= 1
# ===========================ESTADO=S2=================================================
# =======================COMILLAS=DOBLES============================================
            elif estado == "S2":
                # validar las cadenas
                if(letra == '"'):
                    buffer += letra
                    columna += 1
                    # segunda comilla
                    self.Tokenzz.append(
                        Token("cadena", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"  # validar para las comillas y regresa al estado 0
                elif(letra == '\n'):
                    columna = 1
                    linea += 1
                elif(letra == "'"):
                    buffer += letra
                    columna += 1
                    self.errorezz.append(
                        error(buffer, "error lexico", linea, columna))
                    buffer = ""
                    estado = "S0"
                else:
                    buffer += letra
                    columna += 1
                    estado = "S2"
# ======================COMILLAS=SIMPLES===================================
            elif estado == "S3":
                # validar las cadenas
                if(letra == "'"):
                    buffer += letra
                    columna += 1
                    # segunda comilla
                    self.Tokenzz.append(
                        Token("cadena", buffer, linea, columna))
                    buffer = ""
                    estado = "S0"  # validar para las comillas y regresa al estado 0
                elif(letra == '\n'):
                    columna = 1
                    linea += 1
                elif(letra == '"'):
                    buffer += letra
                    columna += 1
                    self.errorezz.append(
                        error(buffer, "error lexico", linea, columna))
                    buffer = ""
                    estado = "S0"

                else:
                    buffer += letra
                    columna += 1
                    estado = "S3"
# ==================================================DIGITOS=AÑO=====
            elif estado == "S4":
                if letra.isdigit():
                    buffer += letra
                    columna += 1
                    estado = 'S4'
                else:

                    self.Tokenzz.append(
                        Token("tk_digito", buffer, linea, columna))
                    buffer = ""
                    contadorzz -= 1
                    estado = "S0"

            contadorzz += 1

    def imprimir(self):
        print("Tokens: ")
        for T in self.Tokenzz:
            T.mostrar()
        print("errores")
        for E in self.errorezz:
            E.mostrar()
        print("cantidad de Tokens: " + str(len(self.Tokenzz)))
        print("cantidad de errores: " + str(len(self.errorezz)))
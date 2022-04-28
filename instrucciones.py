
Database = []


def cargardatos():
    archivo = open("LaLigaBot-LFP.csv", "r", encoding="utf-8")
    while True:
        linea = archivo.readline()
        Data = linea.split(",")

        if len(Data) == 7:
            Data[6] = Data[6].replace("\n", "")
            print(Data)
            nuevo = Liga(Data[0], Data[1], Data[2],
                         Data[3], Data[4], Data[5], Data[6])
            Database.append(nuevo)

        if not linea:
            break
    archivo.close()


cargardatos()


class instruccioninicio():
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones

    def ejecutar(self, entorno):
        self.instrucciones.ejecutar(entorno)


class instruccioninstrucciones():
    def __init__(self, instruccion, instrucciones2):
        self.instruccion = instruccion
        self.instrucciones2 = instrucciones2

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)
        self.instrucciones2.ejecutar(entorno)


class instruccioninstruccion():
    def __init__(self, instruccion):
        self.instruccion = instruccion

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)


class intruccioninstrucciones2():
    def __init__(self, instruccion, instrucciones2):
        self.instruccion = instruccion
        self.instrucciones2 = instrucciones2

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
        if self.instrucciones2:
            self.instrucciones2.ejecutar(entorno)


class resultado():
    def __init__(self, equipo1, equipo2, anio1, anio2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.anio1 = anio1
        self.anio2 = anio2

    def ejecutar(self):  # xd
        global Database
        temporada = str(self.anio1) + "-" + str(self.anio2)
        for i in range(len(Database)):
            if Database[i].temporada == temporada and Database[i].equipo1 == self.equipo1 and Database[i].equipo2 == self.equipo2:
                mensaje = "El resultado de este partido fue: " + \
                    Database[i].equipo1 + " " + Database[i].goles1 + \
                    " - " + Database[i].equipo2 + " " + Database[i].goles2
                print(mensaje)


class joranda():
    def __init__(self,):
        pass

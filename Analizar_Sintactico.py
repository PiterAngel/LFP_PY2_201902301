from instrucciones import *


class Analisis_Sintactico:
    def __init__(self):
        self.listaTokens = []
        self.listaErroresSin = []
        self.listaErroresLex = []
        self.i = 0

    def resultado(self):
        if self.listaTokens[self.i].tipo == "ID_resultado":
            self.i += 1
            if self.listaTokens[self.i].tipo == "cadena":
                self.i += 1
                equipo1 = self.listaTokens[self.i].lexema

                if self.listaTokens[self.i].tipo == "ID_vs":
                    self.i += 1

                    if self.listaTokens[self.i].tipo == "cadena":
                        self.i += 1
                        equipo2 = self.listaTokens[self.i].lexema
                        if self.listaTokens[self.i].tipo == "ID_temporada":
                            self.i += 1
                            if self.listaTokens[self.i].tipo == "menorque":
                                self.i += 1
                                if self.listaTokens[self.i].tipo == "tk_digito":
                                    self.i += 1
                                    anio1 = self.listaTokens[self.i].lexema
                                    if self.listaTokens[self.i].tipo == "guion":
                                        self.i += 1
                                        if self.listaTokens[self.i].tipo == "tk_digito":
                                            self.i += 1
                                            anio2 = self.listaTokens[self.i].lexema
                                            if self.listaTokens[self.i].tipo == "mayorque":
                                                self.i += 1
                                                return resultado(equipo1, equipo2,anio1,anio2)

    def instruccion(self):
        if self.listaTokens[self.i].tipo == "ID_resultado":
            instruccion = self.resultado()
        elif self.listaTokens[self.i].tipo == "ID_jornada":
            instruccion = self.jornada()
        elif self.listaTokens[self.i].tipo == "ID_goles":
            instruccion = self.goles()

    def intrucciones2(self):
        if self.listaTokens.tipo == "Fin de la lectura":
            print("ANALISIS HECHO CON EXITO :0")
        else:
            instruccion = self.instruccion()
            instrucciones2 = None
            if self.i < len(self.listaTokens):
                instrucciones2 = self.intrucciones2()

    def instrucciones(self):
        instrucciones = self.intruccion()
        intrucciones2 = self.instrucciones2()

    def inicio(self):
        instrucciones = self.instrucciones()

    def parsear(self, listaT, listaE):
        self.listaTokens = listaT
        self.listaErroresLex = listaE

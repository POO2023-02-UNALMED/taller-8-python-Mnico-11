from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):

    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil, listaFutbolistas):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)

        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas+=[self]

    def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(Persona.getNombre(self),Deportista.getDeporte(self),Persona.getEdad(self),Deportista.getAñosPracticando(self))

    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil = piernaHabil
    
from led import Led


class Digito:
    posiciones = ["inferiorIzq", "superiorIzq", "superior", "superiorDcho", "inferiorDcho", "inferior", "central"]
    mapaDigitosAPosicionesDeLeds = {0: {"inferiorIzq", "superiorIzq", "superior", "superiorDcho", "inferiorDcho", "inferior"},
                        1: {"superiorDcho", "inferiorDcho"},
                        2: {"inferiorIzq", "superior", "superiorDcho", "inferior", "central"},
                        3: {"superior", "superiorDcho", "inferiorDcho", "inferior", "central"},
                        4: {"superiorIzq", "superiorDcho", "inferiorDcho", "central"},
                        5: {"superiorIzq", "superior", "inferiorDcho", "inferior", "central"},
                        6: {"inferiorIzq", "superiorIzq", "inferiorDcho", "inferior", "central"},
                        7: {"superior", "superiorDcho", "inferiorDcho"},
                        8: {"inferiorIzq", "superiorIzq", "superior", "superiorDcho", "inferiorDcho", "inferior", "central"},
                        9: {"superiorIzq", "superior", "superiorDcho", "inferiorDcho", "central"}
                        }

    def __init__(self):
        self.leds = [ Led(posicion) for posicion in Digito.posiciones ]
        self.ledsAEncender = self.leds
        self.ledsAApagar = set()


    def __repr__(self):
        return f"D:{self.leds}"


    def getLedsAEncender(self, posiciones):
        ledsAEncender = set()
        for led in self.leds:
            if led.posicion in posiciones:
                ledsAEncender.add(led)
        return ledsAEncender
    

    def getLedsAApagar(self, posiciones):
        ledsAApagar = set()
        for led in self.leds:
            if led.posicion in posiciones:
                ledsAApagar.add(led)
        return ledsAApagar


    def getPosicionesDeLedsAEncender(self, numeroARepresentar) -> set:
        return Digito.mapaDigitosAPosicionesDeLeds[numeroARepresentar]


    def setLedsAEncenderYApagar(self, numeroARepresentar):
        posicionesDeLedsEncendidos = {led.posicion for led in self.ledsAEncender}
        posicionesDeLedsAEncender = self.getPosicionesDeLedsAEncender(numeroARepresentar)

        posicionesDeLedsAEncender = posicionesDeLedsAEncender.difference(posicionesDeLedsEncendidos)
        posicionesDeLedsAApagar = posicionesDeLedsEncendidos.difference(posicionesDeLedsAEncender)

        self.ledsAEncender = self.getLedsAEncender(posicionesDeLedsAEncender)
        self.ledsAApagar = self.getLedsAApagar(posicionesDeLedsAApagar)


    def encenderLeds(self):
        gastoEnergetico = 0
        for led in self.ledsAEncender:
            gastoEnergetico += led.encender()
        return gastoEnergetico


    def apagarLeds(self):
        for led in self.ledsAApagar:
            led.apagar()

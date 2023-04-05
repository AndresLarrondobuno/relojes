from led import Led

class Digito:
    mapaDigitosACantidadLeds = {0:6, 1:2, 2:5, 3:5, 4:5, 5:5, 6:5, 7:3, 8:7, 9:5}

    def __init__(self):
        self.leds = [ Led() for x in range(7) ]
        self.ledsAEncender = None


    def __repr__(self):
        return f"D:{self.leds}"


    def getCantidadDeLedsAEncender(self, numeroARepresentar):
        return Digito.mapaDigitosACantidadLeds[numeroARepresentar]
    

    def setLedsAEncender(self, numeroARepresentar):
        self.ledsAEncender = self.leds[:self.getCantidadDeLedsAEncender(numeroARepresentar)]


    def encenderLeds(self):
        gastoEnergetico = 0
        for led in self.ledsAEncender:
            gastoEnergetico += led.encender()
        return gastoEnergetico
    

    def apagar(self):
        for led in self.leds:
            led.apagar()

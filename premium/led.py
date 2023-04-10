class Led:
    def __init__(self, posicion):
        self.encendido = False
        self.posicion = posicion
        self.gastoEnergetico = 1
    

    def __repr__(self) -> str:
        if self.encendido:
            return "T"
        return "F"
    

    def encender(self):
        self.encendido = True
        return self.gastoEnergetico
    

    def apagar(self):
        self.encendido = False
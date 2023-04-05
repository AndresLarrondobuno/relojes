class Led:
    def __init__(self):
        self.encendido = False
        self.gastoEnergetico = 1
    

    def __repr__(self) -> str:
        return f" {self.encendido} "
    

    def encender(self):
        self.encendido = True
        return self.gastoEnergetico
    

    def apagar(self):
        self.encendido = False
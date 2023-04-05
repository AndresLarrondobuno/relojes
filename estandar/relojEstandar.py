from digito import Digito
from convertidorDeUnidades import ConvertidorDeUnidades

class RelojEstandar:
    maximoHoras, maximoMinutos, maximoSegundos = 23, 59, 59

    def __init__(self):
        self.segundosTranscurridos = 0
        self.horas, self.minutos, self.segundos = 0, 0, 0
 
        self.digitos = { 
            'digitosHoras': [Digito(), Digito()],
            'digitosMinutos' : [Digito(), Digito()],
            'digitosSegundos' : [Digito(), Digito()] 
            }
        
        self.digitosHoras = self.digitos['digitosHoras']
        self.digitosMinutos = self.digitos['digitosMinutos']
        self.digitosSegundos = self.digitos['digitosSegundos']    


    def __repr__(self) -> str:
        return f"h: {self.horas} m: {self.minutos} m: {self.segundos}"


    def incrementarSegundo(self):
        self.segundosTranscurridos += 1
        if self.segundos < RelojEstandar.maximoSegundos:
            self.segundos += 1
        else:
            self.segundos = 0
            self.incrementarMinuto()

    
    def incrementarMinuto(self):
        if self.minutos < RelojEstandar.maximoMinutos:
            self.minutos += 1
        else:
            self.minutos = 0
            self.incrementarHora()


    def incrementarHora(self):
        if self.horas < RelojEstandar.maximoHoras:
            self.horas += 1
        else:
            self.horas = 0


    def setDigitos(self):
        valorSexagesimal = ConvertidorDeUnidades.convertirSegundosASexagesimal(self.segundosTranscurridos)
        horas, minutos, segundos = valorSexagesimal['horas'], valorSexagesimal['minutos'], valorSexagesimal['segundos']
        #obtener los numeros a representar de cada digito de cada campo
        numeroARepresentarHoras = ConvertidorDeUnidades.enteroADigitos(horas)
        numeroARepresentarMinutos = ConvertidorDeUnidades.enteroADigitos(minutos)
        numeroARepresentarSegundos = ConvertidorDeUnidades.enteroADigitos(segundos)
        numerosOrdenados = [numeroARepresentarHoras, numeroARepresentarMinutos, numeroARepresentarSegundos]
        
        #con esos numeros setear los digitos
        for campo, numeroARepresentar in zip(self.digitos.keys(), numerosOrdenados):
            self.setDigito(campo, numeroARepresentar)


    def setDigito(self, campo, numerosARepresentar):
        #modificar atributo 'ledsAEncender' de Digito
        self.digitos[campo][0].setLedsAEncender(numerosARepresentar[0])
        self.digitos[campo][1].setLedsAEncender(numerosARepresentar[1])
 

    def encenderDigitos(self):
        gastoEnergetico = 0
        for campo in self.digitos.values():
            for digito in campo:
                gastoEnergetico += digito.encenderLeds()
        return gastoEnergetico
        

    def apagarDigitos(self):
        for campo in self.digitos.values():
            for digito in campo:
                digito.apagar()
    

    def getGastoEnergetico(self, segundos):
        gastoEnergetico = 0

        for segundo in range(segundos + 1):
            self.setDigitos()#setea digitos utilizando los valores enteros de cada campo[(HH),(MM),(SS)]
            for campo in self.digitos.values():
                for digito in campo:
                    gastoEnergetico += digito.encenderLeds() 
            self.incrementarSegundo()
            self.apagarDigitos()

        return gastoEnergetico
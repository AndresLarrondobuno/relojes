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
        return f"{self.horas} : {self.minutos} : {self.segundos}"


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
        numeroARepresentarHoras = ConvertidorDeUnidades.enteroADigitos(horas)
        numeroARepresentarMinutos = ConvertidorDeUnidades.enteroADigitos(minutos)
        numeroARepresentarSegundos = ConvertidorDeUnidades.enteroADigitos(segundos)
        numerosOrdenados = [numeroARepresentarHoras, numeroARepresentarMinutos, numeroARepresentarSegundos]
        
        #con esos numeros setear los digitos
        for campo, numeroARepresentar in zip(self.digitos, numerosOrdenados):
            self.setDigito(campo, numeroARepresentar)
    

    def setDigito(self, campo, numeroARepresentar):
        #obtener el numero a representar de cada digito del campo
        numerosARepresentar = ConvertidorDeUnidades.enteroADigitos(numeroARepresentar)
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
    

    def getGastoEnergetico(self, segundosTranscurridos):
        gastoEnergetico = self.encenderDigitos()#primer pantalla

        for segundo in range(1, segundosTranscurridos):
            self.incrementarSegundo()
            self.setDigitos()
            for digito in self.digitos:
                gastoEnergetico += digito.encenderLeds()#setea digitos utilizando los valores enteros de cada campo
                
        return gastoEnergetico
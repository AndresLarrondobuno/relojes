from digito import Digito
from convertidorDeUnidades import ConvertidorDeUnidades

class RelojPremium:
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
        if self.segundos < RelojPremium.maximoSegundos:
            self.segundos += 1
        else:
            self.segundos = 0
            self.incrementarMinuto()

    
    def incrementarMinuto(self):
        if self.minutos < RelojPremium.maximoMinutos:
            self.minutos += 1
        else:
            self.minutos = 0
            self.incrementarHora()


    def incrementarHora(self):
        if self.horas < RelojPremium.maximoHoras:
            self.horas += 1
        else:
            self.horas = 0
    

    def setDigitos(self):
        valorSexagesimal = ConvertidorDeUnidades.convertirSegundosASexagesimal(self.segundosTranscurridos)
        horas, minutos, segundos = valorSexagesimal['horas'], valorSexagesimal['minutos'], valorSexagesimal['segundos']
        #obtener los numeros a representar de cada digito de cada campo
        numeroARepresentarHoras = ConvertidorDeUnidades.enteroADigitos(horas) #metodo llamado 3 veces considerar for
        numeroARepresentarMinutos = ConvertidorDeUnidades.enteroADigitos(minutos)
        numeroARepresentarSegundos = ConvertidorDeUnidades.enteroADigitos(segundos)
        numerosOrdenados = [numeroARepresentarHoras, numeroARepresentarMinutos, numeroARepresentarSegundos]
        
        #con esos numeros setear los digitos, tener en cuenta que los digitos pueden no necesitar mutar ahora
        for campo, numeroARepresentar in zip(self.digitos.keys(), numerosOrdenados):
            self.setDigito(campo, numeroARepresentar)


    def setDigito(self, campo, numerosARepresentar):
        #modificar atributo 'ledsAEncender' de Digito
        self.digitos[campo][0].setLedsAEncenderYApagar(numerosARepresentar[0])
        self.digitos[campo][1].setLedsAEncenderYApagar(numerosARepresentar[1])


    def getGastoEnergetico(self, segundos):
        gastoEnergetico = 0
        
        for segundo in range(segundos + 1):
            self.setDigitos()
            for campo in self.digitos.values():
                for digito in campo:
                    gastoEnergetico += digito.encenderLeds()
                    digito.apagarLeds()
            self.incrementarSegundo()

        return gastoEnergetico

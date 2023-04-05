class ConvertidorDeUnidades:

    def convertirSegundosASexagesimal(segundos):
        horas = segundos // 3600
        segundos_restantes = segundos - horas * 3600
        minutos = segundos_restantes // 60
        segundos -= minutos * 60
        return {"horas":horas, "minutos":minutos, "segundos":segundos}


    def enteroADigitos(entero):
        primerDigito = entero // 10
        segundoDigito = entero % 10
        return [primerDigito, segundoDigito]
from digito import Digito

cero = Digito.mapaDigitosAPosicionesDeLeds[0]
uno = Digito.mapaDigitosAPosicionesDeLeds[1]
dos = Digito.mapaDigitosAPosicionesDeLeds[2]
tres = Digito.mapaDigitosAPosicionesDeLeds[3]
cuatro = Digito.mapaDigitosAPosicionesDeLeds[4]

diferenciaCuatroTres = cuatro.difference(tres)
diferenciaTresCuatro = tres.difference(cuatro)

print(f"Interseccion: {diferenciaCuatroTres}")
print(f"Diferencia: {diferenciaTresCuatro}")


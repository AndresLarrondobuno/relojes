from estandar.relojEstandar import RelojEstandar
from premium.relojPremium import RelojPremium

if __name__ == "__main__":
    relojEstandar, relojPremium = RelojEstandar(), RelojPremium()
    gastoDiarioDeRelojEstandar = relojEstandar.getGastoEnergetico(86400)
    gastoDiarioDeRelojPremium = relojPremium.getGastoEnergetico(86400)

    ahorroDiario = gastoDiarioDeRelojEstandar - gastoDiarioDeRelojPremium
    print(ahorroDiario)

class convinatoria:
    #Formulas
    FORMULAVARICIONSINREPETICION = "int(self.factorial(self.CantidadDeObjetos) / self.factorial(self.CantidadDeObjetos - self.CantidadDeObjetosPorGrupo))"
    FORMULAVARICIONCONREPETICION = "int(self.CantidadDeObjetos ** self.CantidadDeObjetosPorGrupo)"
    FORMULAPERMUTACIONSINREPETICION = "int(self.factorial(self.CantidadDeObjetos))"
    FORMULAPERMUTACIONCONREPETICION = "int(self.CantidadDeObjetos ** self.CantidadDeObjetos)"
    FORMULACONVINATORIASINREPETICION = "int(self.factorial(self.CantidadDeObjetos) / (self.factorial(self.CantidadDeObjetosPorGrupo) * self.factorial(self.CantidadDeObjetos - self.CantidadDeObjetosPorGrupo)))"
    FORMULACONVINATORIACONREPETICION = "int(self.factorial((self.CantidadDeObjetos + self.CantidadDeObjetosPorGrupo - 1)) / (self.factorial(self.CantidadDeObjetosPorGrupo) * self.factorial(self.CantidadDeObjetos - 1)))"

    listaFormula = [FORMULAVARICIONSINREPETICION,FORMULAVARICIONCONREPETICION,FORMULAPERMUTACIONSINREPETICION,FORMULAPERMUTACIONCONREPETICION,FORMULACONVINATORIASINREPETICION,FORMULACONVINATORIACONREPETICION]

    def __init__(self, CantidadDeObjetos, CantidadDeObjetosPorGrupo):
        self.CantidadDeObjetos = CantidadDeObjetos
        self.CantidadDeObjetosPorGrupo = CantidadDeObjetosPorGrupo

    def factorial(self, number:int):
        for i in range(number-1,1,-1): number *= i
        return number if number != 0 else 1
    
    def calcular(self,FORMULA):
        return eval(self.listaFormula[FORMULA-1]) if (FORMULA > 0 and FORMULA < 7) else "Error elegiste algo que no existe"

if __name__ == "__main__":
    h = convinatoria(int(input("cantidad de objetos")),int(input("cantidad de objetos por grupo")))
    print(h.calcular(int(input("""Eliga que opcion quiere:
    Variacion sin repeticion: 1
    Variacion con repeticion: 2
    Permutacion sin repeticion: 3
    Permutacion con repeticion: 4
    Convinatoria sin  repeticion: 5                                                         
    Convinatoria con  repeticion: 6
    """))))
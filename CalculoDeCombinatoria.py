#es lo mismo que el main nada mas que pensado solo como libreria anque el main tambien funcinaria
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
        if (FORMULA>0 and FORMULA<7):
            if (FORMULA%2 != 1):
                return "Error ya que elegiste una opcion sin repeticion y los grupos contienen mas elementos que los conjuntos"
            else:
                return eval(self.listaFormula[FORMULA-1])
        else:
            return "Error ya que elegiste un valor fuera de las opciones" 

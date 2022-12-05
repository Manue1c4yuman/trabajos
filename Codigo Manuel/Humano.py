from Personaje import Personaje 

class Humano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida=0.0, daño="", bonificacion="",familia=""):
        super().__init__(nombre="", raza="", arma="", vida=0.0, daño="", bonificacion="")
        self.__familia = familia 

    def __str__(self):
         return super().__str__()+"familia: {} ".format(self.__familias)

    def getfamilia(self):
        return self.__familia 
    def setfamilia(self, familia):
        self.__familia = familia 
        

#historia
#victoria 
#derrota 
#superbono 
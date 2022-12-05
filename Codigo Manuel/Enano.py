from Personaje import Personaje 

class Enano(Personaje):
    def __init__(self,nombre="", raza="", arma="", vida=0.0, daño="", bonificacion="", clan=""):
        super().__init__(nombre="", raza="", arma="", vida=0.0, daño="", bonificacion="")
        self.__clan = clan 

    def __str__(self):
         return super().__str__()+"clan: {}".format(self.__clan)

    def getclan(self):
        return self.__clan 
    def setclan(self, clan):
        self.__clan = clan 

        #Historia 
        #Vicotira 
        #derrota
        #aumentavida

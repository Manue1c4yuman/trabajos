from Personaje import Personaje

class Elfo(Personaje):
    def __init__(self,nombre="", raza="", arma="", vida=0.0, daño="", bonificacion="", reino="" ):
        super().__init__(nombre="", raza="", arma="", vida=0.0, daño="", bonificacion="")
        self.__reino = reino 

    def __str__(self):
        return super().__str__()+"reino{}".format(self.__reino)


    def getreino(self):
        return self.__reino 
    def setereino(self, reino):
        self.__reino = reino 

    #Historia 
    #victoria 
    #derrota
    #quitavida

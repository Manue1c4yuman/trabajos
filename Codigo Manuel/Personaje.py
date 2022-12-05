class Personaje():

    def __init__(self,nombre="", raza="", arma="", vida=0.0, daño="", bonificacion=""):
        self.__nombre = nombre 
        self.__raza = raza 
        self.__arma = arma
        self.__vida = vida 
        self.__daño = daño 
        self.__bonificacion = bonificacion 

    def __str__(self):
        return "nombre: {} raza: {} arma: {} vida: {} daño: {} bonificacion: {}".format(self.__nombre , self.__raza, self.__arma, self.__vida, self.__daño, self.__bonificacion)

    def Getnombre(self):
        return self.__nombre
    def Getnombre(self, nombre):
        self.__nombre = nombre  

    def Getraza(self):
        return self.__raza
    def Setraza(self, raza):
        self.__raza = raza

    def Getarma(self):
        return self.__arma
    def Setarma(self, arma):
        self.__arma = arma

    def Getvida(self):
        return self.__vida
    def Setvida(self, vida):
        self.__vida = vida 

    def Getdaño(self):
        return self.__daño 
    def Setdaño(self, daño):
        self.__daño = daño 
        
    def Getbonificacion(self):
        return self.__bonificacion
    def Setbonificacion(self, bonificacion):
        self.__bonificacion = bonificacion       
    
    def atributos(self):
        print(self.__nombre)
        print("Raza:",self.__raza)
        print("Arma:", self.__arma)
        print("vida: ", self.__vida)
        print("Daño: ", self.__daño)
        print("La bonificacion es: ", self.__bonificacion)

    def vivo(self):
        return self.__vida > 0 
    
    def morir(self):
        self.__vida = 0 
        print (self.__nombre, "Ha muerto")
    
    def daño (self, ememigo):
        return self.__fuerza - enemigo.__defensa 
    
    def atacar(self, enemigo):
        daño =  self.__daño (enemigo)
        enemigo.__vida = enemigo.__vida - daño 
        print (self.__nombre, "ha realizado", daño, "puntos de daño a" , enemigo.__nombre)
        if enemigo.__vivo():
            print("La vida de ", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()


#mi_personaje = Personajes("mano", 10, 1, 5,  100 )
#mi_enemigo = Personajes ("platano", 8, 5, 3, 5)


#historia:
#victoria
#derrota 
#mensajeinicial 

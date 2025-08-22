class Personaje:
    nombre = "Default"  #ESTOS SON LOS ATRIBUTOS
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 100
    #EL INIT ES EL CONSTRUCTOR
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida): #LOS DEF SON LOS METODOS
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida


    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".Fuerza", self.fuerza)
        print(".Inteligencia", self.inteligencia)
        print(".Defensa", self.defensa)
        print(".Vida", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa 
    
    def esta_vivo(self):
        return self.vida > 0
    
    def __morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ataca a", enemigo.nombre, "y le hace", daño, "puntos de daño.")
        if enemigo.esta_vivo():
            print(enemigo.nombre, "sigue vivo con", enemigo.vida, "puntos de vida.")
        else:
            enemigo.__morir()

#AHORA PARA LLAMAR A LA CLASE, HAY QUE AÑADIRLE LOS PARAMETROS  DE NUESTRO CONSTRUCTOR
#EN ESTE CASO SERIA, EL NOMBRE, FUERZA, INTELIGENCIA, DEFENSA Y VIDA, SIEMPRE SE IGNORA EL "SELF"
mi_personaje = Personaje("DaFer", 10, 10, 10, 100)
mi_enemigo = Personaje("Gabox", 8, 8, 8, 80)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()

class pene:
    pass

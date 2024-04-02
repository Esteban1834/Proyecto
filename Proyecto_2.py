class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque

    def ejecutar_ataque(self):
        pass


# Describe el comportamiento de ataque para los pokemones
class AtaquePikachu:
    def ejecutar_ataque(self):
        print("Pikachu ataca con Impactrueno, Rayo, ataque rapido o placaje.")


class AtaqueCaterpie:
    def ejecutar_ataque(self):
        print("Caterpie ataca con placaje, tacleada, supersonico o drenadoras.")

class AtaquePidgeotto:
    def ejecutar_ataque(self):
        print("Pidgeotto ataca con picotazo, remolino, tornado o ataque rapido.")

class AtaqueBulbasaur:
    def ejecutar_ataque(self):
        print("Bulbasur ataca con latigo cepa, drrnadoras, placaje o somnilfero.")
class AtaqueCharmander:
    def ejecutar_ataque(self):
        print("Charmander ataca con lanzallamas, gruñido, aranazo o ascuas.")
class AtaqueSquirtle:
    def ejecutar_ataque(self):
        print("Squirtle ataca con pistola agua, burbuja, ataque rapido o placaje.")
class AtaqueKrabby:
    def ejecutar_ataque(self):
        print("Krabby ataca con burbuja, rayo burbuja, placaje o tajo cruzado.")
class AtaqueRaticate:
    def ejecutar_ataque(self):
        print("Raticate ataca con hipercolmillo, ataque rapido, placaje o golpe cabeza.")
class AtaqueMuk:
    def ejecutar_ataque(self):
        print("Muk ataca con lodo, bomba lodo, ataque acido o infortunio.")
class AtaqueKingler:
    def ejecutar_ataque(self):
        print("Kingler ataca con hidropulso, rayo burbuja, rayo o placaje.")

# Clase Picachu que hereda de Pokemon
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaquePikachu())
class Caterpie(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaqueCaterpie())        
class Pidgeotto(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaquePidgeotto())
class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaqueBulbasaur())
class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaqueCharmander())
class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaqueSquirtle())
class Krabby(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaqueKrabby())   
class Raticate(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaqueRaticate())
class Muk(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaqueMuk())
class Kingler(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", AtaqueKingler())     
        
                                                        




# Ejemplo de uso
pikachu = Pikachu()
caterpie = Caterpie()
pidgeotto = Pidgeotto()
bulbasaur = Bulbasaur()
charmander = Charmander()
squirtle = Squirtle()
krabby = Krabby()
raticate = Raticate()
muk = Muk()
kingler = Kingler()


# Soldado realiza ataque
pikachu.ataque.ejecutar_ataque()
caterpie.ataque.ejecutar_ataque()
pidgeotto.ataque.ejecutar_ataque()
bulbasaur.ataque.ejecutar_ataque()
charmander.ataque.ejecutar_ataque()
squirtle.ataque.ejecutar_ataque()
krabby.ataque.ejecutar_ataque()
raticate.ataque.ejecutar_ataque()
muk.ataque.ejecutar_ataque()
kingler.ataque.ejecutar_ataque()




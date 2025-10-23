class Tamagotchi: 
    def __init__(self, energyMax: int, cleanMax: int):
        self.__energyMax: int = energyMax
        self.__cleanMax: int = cleanMax
        self.__energy: int = energyMax
        self.__clean: int = cleanMax
        self.__age: int = 0
        self.__alive: bool = True

    def set_energy(self, valor: int) -> None:
        self.__energy = valor
        if self.__energy <= 0: 
            self.__energy = 0
            self.__alive = False
            print("fail: pet morreu de fraqueza")
            return
        if self.__energy > self.__energyMax:
            self.__energy = self.__energyMax

    def set_clean(self, valor: int) -> None:
        self.__clean = valor
        if valor > self.__cleanMax:
            self.__clean = self.__cleanMax
        if valor == 0:
            self.__alive = False

    def set_age(self, valor: int) -> None:
        self.__age = valor

    def get_clean(self) -> int:
        return self.__clean
    def get_cleanMax(self) -> int:
        return self.__cleanMax
    def get_energy(self) -> int:
        return self.__energy
    def get_energyMax(self) -> int:
        return self.__energyMax
    def get_age(self) -> int:
        return self.__age
        
    def isAlive(self) -> bool:
        return self.__alive

    def __str__(self) -> str:
        return f"E:{self.__energy}/{self.__energyMax}, L:{self.__clean}/{self.__cleanMax}, I:{self.__age}"

class Game:
    def __init__(self, pet: Tamagotchi):
        self.__pet: Tamagotchi = pet

    def play(self) -> None:
        if self.__pet.isAlive() == False:
            print("fail: pet esta morto")
            return
        self.__pet.set_energy(self.__pet.get_energy() - 2)
        self.__pet.set_clean(self.__pet.get_clean() - 3)
        self.__pet.set_age(self.__pet.get_age() + 1)
        if self.__pet.get_clean() <= 0:
            print("fail: pet morreu de sujeira")
            self.__pet.set_clean(0)
            self.__pet.isAlive() == False

    def sleep(self) -> None:
        if self.__pet.isAlive() == False:
            print("fail: pet esta morto")
            return
        if self.__pet.get_energy() >= self.__pet.get_energyMax() - 5:
            print("fail: nao esta com sono")
            return
        if self.__pet.get_energy() == 0:
            print("fail: pet morreu de fraqueza")
            return
        self.__pet.set_energy(self.__pet.get_energyMax())
        self.__pet.set_age(self.__pet.get_age() + 6)
    
    def shower(self) -> None:
        if self.__pet.isAlive() == False:
            print("fail: pet esta morto")
            return
        self.__pet.set_energy(self.__pet.get_energy() - 3)
        self.__pet.set_clean(self.__pet.get_cleanMax())
        self.__pet.set_age(self.__pet.get_age() + 2)
        
    def __str__(self) -> str:
        return str(self.__pet)

def main():
    pet = None
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pet)
        elif args[0] == "init":
            energy = int(args[1])
            clean = int(args[2])
            pet = Tamagotchi(energy, clean)
            pet = Game(pet)
        elif args[0] == "play":
            pet.play()
        elif args[0] == "sleep":
            pet.sleep()
        elif args[0] == "shower":
            pet.shower()
        else:
            print("fail: comando invalido")

main()
class Watch:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.set_hora(int(hora))
        self.set_minuto(int(minuto))
        self.set_segundo(int(segundo))


    def get_hora(self) -> int:
        return self.__hora
    def get_minuto(self) -> int:
        return self.__minuto
    def get_segundo(self) -> int:
        return self.__segundo


    def set_hora(self,  valor: int) -> None:
        if valor > 23 or valor < 0:
            print("fail: hora invalida")
            return 
        self.__hora = valor
    def set_minuto(self,  valor: int) -> None:
        if valor > 59 or valor < 0:
            print("fail: minuto invalido")
            return
        self.__minuto = valor
    def set_segundo(self,  valor: int) -> None:
        if valor > 59 or valor < 0:
            print("fail: segundo invalido")
            return
        self.__segundo = valor


    def nextSecond(self, increment: int = 1) -> None:
        self.__segundo += increment
        if self.__segundo >= 60:
            self.__segundo = 0
            self.__minuto += increment
        if self.__minuto >= 60:
            self.__minuto = 0
            self.__hora += increment
        if self.__hora >= 24:
            self.__hora = 0


    def __str__(self) -> str:
        return f"{self.__hora:02}:{self.__minuto:02}:{self.__segundo:02}"


def main():
    relogio = Watch(0, 0, 0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(relogio)
        elif args[0] == "set":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio.set_hora(hora), 
            relogio.set_minuto(minuto), 
            relogio.set_segundo(segundo)
        elif args[0] == "init":
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio = Watch(hora, minuto, segundo)
        elif args[0] == "next":
            if len(args) == 1:
                relogio.nextSecond()
            else:
                increment = int(args[1])
                relogio.nextSecond(increment)
        else:
            print("comando invalido")

main()
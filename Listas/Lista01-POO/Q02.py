class Viagem:
    def __init__(self):
        self.distancia = 0
        self.tempo = 0
    def calc_velocidademedia(self):
        return self.distancia / self.tempo

x = Viagem()
x.distancia = int(input("Digite a distância percorrida: "))
x.tempo = int(input("Digite o tempo gasto: "))
print(f"Velocidade média = {x.calc_velocidademedia()}")

class Circulo:
    def __init__(self):
        self.raio = 0
    def calc_area(self):
        return 3.14 * (self.raio**2)
    def calc_circunferencia(self):
        return 2 * 3.14 * self.raio
x = Circulo()
x.raio = int(input("Digite o raio do círculo: "))
print(f"Área = {x.calc_area()}")
print(f"Circunferência = {x.calc_circunferencia()}")

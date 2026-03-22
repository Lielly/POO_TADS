print("Digite quatro valores inteiros diferentes")
w = int(input())
x = int(input())
y = int(input())
z = int(input())
ma = 0
me = 0
if w == x or w == y or w == z or x == y or x == z or y == z:
    print("Erro: os números não são diferentes")
else:
    if w > x and w > y and w > z:
        ma = w
    elif  x > w and x > y and x > z:
        ma = x
    elif y > w and y > x and y > z:
        ma = y
    elif z > w and z > x and z > y:
        ma = z
    if w < x and w < y and w < z:
        me = w
    elif  x < w and x < y and x < z:
        me = x
    elif y < w and y < x and y < z:
        me = y
    elif z < w and z < x and z < y:
        me = z
    so = w + x + y + z - (ma + me)
    print(f"Maior valor = {ma}")
    print(f"Menor valor = {me}")
    print(f"A soma do segundo maior com o segundo menor = {so}")
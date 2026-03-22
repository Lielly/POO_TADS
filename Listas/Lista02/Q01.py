print("Digite quatro valores inteiros")
w = int(input())
x = int(input())
y = int(input())
z = int(input())
l = []
l.append(w)
l.append(x)
l.append(y)
l.append(z)
sp = 0
si = 0
for i in range(len(l)):
    if l[i] % 2 == 0:
        sp = sp + l[i]
    else:
        si = si + l[i]

print(f"Soma dos pares = {sp}")
print(f"Soma dos ímpares = {si}")
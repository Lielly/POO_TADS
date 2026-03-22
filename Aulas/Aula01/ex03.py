x= 5
y= 5

print(id(x))
print(id(y))

x = [1, 2, 3]
y = [1, 2, 3]
x.append(4)
print(x) # 1, 2, 3, 4
print(y) # 1, 2, 3, 4
print(id(x))
print(id(y))

x = [1, 2, 3]
print("Lista X", id(x))
y = [1, 2, 3]
x.append(4)
print("Lista X", id(x))
print(x)
print(y)
print("Lista X", id(x))
print(id(y))
print(x[0])
x[0] = 0
print(x)
print(id(x))

s = "TADS"
print(s[0])
print(id(s))
# s[0] = "W" # Erro
s = "WADS"
print(id(s))
t = "WADS"
print(id(t))
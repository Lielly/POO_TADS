print("Informe o número do mês")
m = int(input())
n = [0, "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
t = ""

if m <= 3:
    t = "primeiro"
elif m > 3 and m <= 6:
    t = "segundo"
elif m > 6 and m <= 9:
    t = "terceiro"
elif m > 9 and m <= 12:
    t = "quarto"

print(f"O mês de {n[m]} é do {t} trimestre do ano")
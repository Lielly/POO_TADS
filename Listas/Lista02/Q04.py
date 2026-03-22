print("Digite uma data no formato dd/mm/aaaa")
d, m, a = map(int, input().split("/"))
mi = [1, 3, 5, 7, 8, 10, 12]
mp = [4, 6, 9, 11]
b = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]
if d < 1 or m < 1 or m > 12 or a < 1900 or a > 2100:
    print("A data informada não é válida")
elif a in b and m == 2 and d > 29:
    print("A data informada não é válida")
elif a not in b and m == 2 and d > 28:
    print("A data informada não é válida")
elif m in mi and d > 31:
    print("A data informada não é válida")
elif m in mp and d > 30:
    print("A data informada não é válida")
else:
    print("A data informada é válida")
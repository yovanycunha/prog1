# coding: utf-8
# Mais Velhos Primeiro
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def idosos_inicio(fila):
	count = 0
	aux = 0
	tem_menor = False
	for i in range(len(fila)):
		if fila[i] < 60:
			tem_menor = True
			break	
	if tem_menor:	
		for i in range(len(fila)):
			if fila[i] >= 60:
				aux = fila[i]
				fila[i] = fila[count]
				fila[count] = aux
				count += 1
				while fila[count] >= 60:
					count += 1

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]

fila = []
idosos_inicio(fila)
assert fila == []

fila = [1,2,3,4]
idosos_inicio(fila)
assert fila == [1,2,3,4]

fila = [1,1,1,1,60,60,60]
idosos_inicio(fila)
assert fila == [60,60,60,1,1,1,1]

fila = [60,61,62,63,64,65]
idosos_inicio(fila)
assert fila == [60,61,62,63,64,65]




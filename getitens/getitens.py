# coding: utf-8
# Get Itens
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def get_items(valores,indices):
	lista = []
	if len(valores) == 0 and len(indices) == 0:
		return lista
	elif len(valores) == 0 and len(indices) > 0:
		for i in range(len(indices)):
			lista.append(None)
		return lista
	else:
		for meu_indice in indices:
			if meu_indice > len(valores) or meu_indice < (len(valores)*-1):
				lista.append(None)
			else:
				lista.append(valores[meu_indice])
		return lista

valores = [18, 22, 73, 32, 19, 21, 43]
indices = [3, 4, 8, 1]
assert get_items(valores, indices) == [32, 19, None, 22]

valores = [1, 2, 3, 4, 5, 6, 7]
indices = [12, 9, 8, 13]
assert get_items(valores, indices) == [None, None, None, None]

valores = [0, 0, 0 , 0 , 0 , 0]
indices = [3, 4, 0, 1]
assert get_items(valores, indices) == [0, 0, 0, 0]


valores = [1, 2, 5 , 6 , 10 , 100]
indices = [-2, 4, 0, -1]
assert get_items(valores, indices) == [10, 10, 1, 100]

valores = []
indices = [-2, 4, 0, -1] 
assert get_items(valores, indices) == [None, None, None, None]


valores = [1, 2, 5 , 6 , 10 , 100]
indices = []
assert get_items(valores, indices) == []


valores = []
indices = []
assert get_items(valores, indices) == []


valores = [1, 2, 5 , 6 , 10 , 100]
indices = [-6]
assert get_items(valores, indices) == [1]

valores = [18, 22, 73, 32, 19, 21, 43]
indices = [3,3, 4, 8, 1, 3]
assert get_items(valores, indices) == [32,32, 19, None, 22,32]


# coding: utf-8
# Herão
# (C) 2016, Yovany Cunha / UFCG, Programação 1
import math

n = int(raw_input(''))
area = 0.0
s = 0.0
cont_maior = 0
area_maior = 0.0
area_maior_media = 0.0

for i in range(1,n+1):
	ladoA,ladoB,ladoC = raw_input('').split(" ")
	ladoA = float(ladoA)
	ladoB = float(ladoB)
	ladoC = float(ladoC)
	s = (ladoA + ladoB + ladoC)/2
	area = math.sqrt(s*(s - ladoA)*(s - ladoB)*(s - ladoC))
	if area > 100:
		cont_maior += 1
		area_maior += area
	print 'Área %d: %.2f' % (i,area)
if cont_maior > 0:
	area_maior_media = area_maior/cont_maior
	print 'Número maiores: %d, área média: %.2f' % (cont_maior,area_maior_media)

# coding: utf-8

print "== Estágio 1 =="

Peso1 = float(raw_input("Peso? "))
Nota1 = float(raw_input("Nota? "))

print "== Estágio 2 =="

Peso2 = float(raw_input("Peso? "))
Nota2 = float(raw_input("Nota? "))

print "== Estágio 3 =="

Peso3 = float(raw_input("Peso? "))
Nota3 = float(raw_input("Nota? "))

media_parcial = (Nota1*Peso1) + (Nota2*Peso2) + (Nota3*Peso3)/(Peso1 + Peso2 + Peso3)

media_minima = (5 - media_parcial * 0.6)/0.4
media_maxima = (7 - media_parcial * 0.6)/0.4

print ("== Resultados ==")
print ("Média parcial: %.1f") % (media_parcial)
print ("Nota na final, pra média 5.0 = %.1f") % (media_minima)
print ("Nota na final, pra média 7.0 = %.1f") % (media_maxima)

# PROYECTO 1: calcular salario semanal en cuanto a horas trabajadas

nombre = input("Ingrese su nombre completo: ")

print ("Hola ",nombre +"!")

horas_trabajadas = float ( input ("Cuantas horas trabajo esta semana: "))
valor_hora = float ( input ("Indique el valor de la hora de trabajo: "))

sueldo = horas_trabajadas * valor_hora

print ("Usted deberia de cobrar ",str(sueldo) +"pesos esta semana")

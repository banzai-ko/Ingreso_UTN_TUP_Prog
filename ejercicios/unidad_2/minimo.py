contador=0
min_numero = 2**31
while(contador<4):
  print("Ingrese un numero")
  num = int(input())
  if num < min_numero:
    min_numero = num
  contador+=1
print("ejecuciones: ",contador)
print("el valor minimo es:", min_numero)
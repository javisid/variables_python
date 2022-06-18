# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''
print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print('Ingrese el primer numero')
numero_1 = float(input())
print('Ingrese el segundo numero')
numero_2 = float(input())

SUMA = numero_1 + numero_2
RESTA = numero_1 - numero_2
DIVISION = numero_1 / numero_2
MULTIPLICACION = numero_1 * numero_2
DIVISION = numero_1 / numero_2
POTENCIA = numero_1 ** numero_2


print('La suma de los numeros ingresados es =',SUMA)
print('La resta de los numeros ingresados es =',RESTA)
print('La division de los numeros ingresados es =',DIVISION)
print('El multiplo de los numeros ingresados es =', MULTIPLICACION)
print('La potencia de los numeros ingresados es =',POTENCIA)
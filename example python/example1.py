"""
    Nombre: Laura Sanchez
    Fecha: 18/09/2023
    Objetivo: ejemplo de versionamiento con git desde python
"""
import random
print("numero aleatorio entre 1 y 10")

random_number = random.randint(1 , 10) #para un numero aleatorio
print(random_number)

for i in range (0, 10):
    random_number = random.randrange(20, 100, 5)
    print(random_number)

print("-----------------------")

for i in range (0, 10): 
    random_number = random.random()  #genera numeros aleatorios de 0 a 10
    print(random_number)

print("-----------------------")

for i in range (0, 10):
    random_number = random.uniform(10.5, 20.6) #genera numeros aleatorios desde decimales
    print(random_number)
#Autor:  Daniele Penaque   
#Data: 21/05/2022

#Importando tabuada
import math

import os
os.system('cls')

#Entrada
numero_1 = int(input('Digite o 1º número: '))
numero_2 = int(input('Digite o 2º número: '))
numero_3 = int(input('Digite o 3º número: '))

#Saída
print('Encontrando o maior: ')
print()
if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'{numero_1} é o maior')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'{numero_2} é o maior')
elif numero_3 > numero_1 and numero_3 > numero_2:
    print(f'{numero_3} é o maior')

print('='*25)
print('Encontrando o menor: ')
print()

if numero_1 < numero_2 and numero_1 < numero_3:
    print(f'{numero_1} é o menor')
elif numero_2 < numero_1 and numero_2 < numero_3:
    print(f'{numero_2} é o menor')
elif numero_3 < numero_1 and numero_3 < numero_2:
    print(f'{numero_3} é o menor')

#Autor:  Daniele Penaque   
#Data: 21/05/2022

#Importando tabuada
import math

import os
os.system('cls')

#Entrada
inteiro = int(input('Digite um número inteiro: '))

#Condição
if inteiro %2 ==0:
    print(f'{inteiro} é um número par')
else: 
    print(f'{inteiro} é um número impar')

#finalizando 
print('='*40)
print('Fim do programa!')
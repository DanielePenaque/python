#Autor:  Daniele Penaque   
#Data: 21/05/2022

#Importando tabuada
import math

import os
os.system('cls')


#Entrada
salario = float(input('Digite o seu salário: '))

maior_salario = salario *0.05
menor_salario = salario *0.10

#Condição
if salario <=0:
    print('Salário Inválido!')
elif salario <1000:
    print(f'o seu salário terá um reajuste de {menor_salario} reais')
else:
     salario >1500
     print(f'O seu salário terá um reajuste de {maior_salario} reais')

#finalizando
print('='*40)
print()
print('Fim do programa!')

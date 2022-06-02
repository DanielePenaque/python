#Autor:  Daniele Penaque   
#Data: 21/05/2022

#Importando tabuada
import math

import os
os.system('cls')

#Entrada
distancia = float(input('Digite a distancia de Juiz de Fora até São Paulo: '))

#Calculo 
if distancia <=0:
    print('Km inválido')
elif distancia <= 200:
    passagem = distancia * 0.7
    print(f'A passagem custará {passagem:.2f} reais')
else:
    passagem_desconto = distancia *0.4
    print(f'A passagem custará {passagem_desconto:.2f} reais')

print('='*50)
print('Fim do programa!')

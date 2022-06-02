#Autor:  Daniele Penaque   
#Data: 21/05/2022

#Importando tabuada
import math

import os
os.system('cls')


#Entrada
velocidade = float(input('Digite a velocidade do carro: '))

#Condição
if velocidade > 200:
    print('Velocidade incorreta!')
elif velocidade >60: 
    print('Você está acima da velocidade')
elif velocidade <=0:
    print('O carro está parado!')
else:
    velocidade <=60 
    print('Você está na velocidade correta!')

#Finalizando
print()
print('Fim do programa!')
print('='*50)


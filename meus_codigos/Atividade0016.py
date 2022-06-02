#Autor:  Daniele Penaque   
#Data: 21/05/2022

#Importando tabuada
import math

import os
os.system('cls')

ano = int(input('Digite um ano: '))

#condição
if ano <=0 or ano >2022:
    print('Ano inválido!')

elif ano %4 == 0:
    print('Ano bissexto')
elif ano %1 >=1:
    print('Ano bissexto')
else:
    print('Ano não bissexto')

#Finalizando
print ()
print('='*50)
print('Fim do programa!')
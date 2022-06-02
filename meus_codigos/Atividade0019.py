#Autor:  Daniele Penaque   
#Data: 21/05/2022

#Importando tabuada
import math

import os
os.system('cls')

#Entrada
Raiz_quadrada = float(input('Digite um valor para raiz quadrada: '))


#Condição
if Raiz_quadrada <=0:
    print('número complexo!')
elif Raiz_quadrada %2 >=0.1: 
    arredonda_para_cima = math.ceil(Raiz_quadrada)
    calculo_raiz1 = math.sqrt(arredonda_para_cima)
    #Mostrando o arredondamento
    print(f'{Raiz_quadrada} passou para {arredonda_para_cima} ')
    print(f'a raiz quadrada de {arredonda_para_cima} é : {calculo_raiz1:.2f}')
else:
    calculo_raiz = math.sqrt(Raiz_quadrada)
    print(f'a raiz quadrada de {Raiz_quadrada} é : {calculo_raiz:.2f}')

#finalizando
print()
print('='*40)
print('Fim do programa!')
#Autor:  Daniele Penaque   
#Data: 02/06/2022

import os
os.system('cls')

#Entrada
frase = str(input('Digite uma frase: '))

#Buscando as vogais

a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

#Saida
print(f'a: {a}')
print(f'e: {e}')
print(f'i: {i}')
print(f'o: {o}')
print(f'u: {u}')

#Finalizando
print('='*40)
print('Fim do programa!')
#Autor: Daniele Penaque
#Data: 17/05/2022
#Uso do comando input

#Entrada
nome = str(input('Qual o seu nome: ')) #cadeia de caracter 
data_nascimento = int(input('Em que ano você nasceu: ')) #inteiro
altura = float(input('Qual a sua altura: ')) #numero com casas decimais
peso = float(input('Quanto você pesa: ')) 


#Saída
print('-'*40)
print('ESTUDO DE ENTRADA DE DADOS COM INPUT')
print ('='*40)
print('Seu nome é:', nome)
print('Ano de nascimento: ', data_nascimento)
print('Você mede: ', altura, 'm')
print('Seu peso é: ', peso, 'Kg')
print('='*40)
print('Fim do Programa!')
print('-'*40)
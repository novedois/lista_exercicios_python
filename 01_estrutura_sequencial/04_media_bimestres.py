'''
-------------------------------------------------------------------------
04. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
-------------------------------------------------------------------------
Estrutura Sequencial

Source...: Python Brasil
URL......: https://wiki.python.org.br/EstruturaSequencial
Data.....: 02.07.2022
Estudante: Filipe Azoubel
-------------------------------------------------------------------------
'''

print('\n* * * * Média * * * *\n')

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
nota_4 = float(input('Digite a quarta nota: '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f'\nA média foi de: {media:.2f}\n')

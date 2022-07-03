'''
-------------------------------------------------------------------------
06. Faça um Programa que peça o raio de um círculo, calcule e mostre sua
    área.
-------------------------------------------------------------------------
Estrutura Sequencial

Source...: Python Brasil
URL......: https://wiki.python.org.br/EstruturaSequencial
Data.....: 02.07.2022
Estudante: Filipe Azoubel
-------------------------------------------------------------------------
'''

import math

print('\n* * * * Área Círculo * * * *\n')

raio = float(input('Digite o raio: '))
area = math.pi * (raio ** 2)

print(f'\nÁrea do círculo: {area:.2f}\n')

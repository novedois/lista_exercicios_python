'''
-------------------------------------------------------------------------
07. Faça um Programa que calcule a área de um quadrado, em seguida mostre
    o dobro desta área para o usuário.
-------------------------------------------------------------------------
Estrutura Sequencial

Source...: Python Brasil
URL......: https://wiki.python.org.br/EstruturaSequencial
Data.....: 03.07.2022
Estudante: Filipe Azoubel
-------------------------------------------------------------------------
'''

print('\n* * * * Dobro da Área * * * *\n')

lado = int(input('Digite o tamanho do lado: '))
area = lado ** 2
dobro_area = area * 2

print(f'\nÁrea: {area}')
print(f'Dobro da área: {dobro_area}\n')

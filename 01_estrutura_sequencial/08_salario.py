'''
-------------------------------------------------------------------------
08. Faça um Programa que pergunte quanto você ganha por hora e o número
    de horas trabalhadas no mês. Calcule e mostre o total do seu salário
    no referido mês.
-------------------------------------------------------------------------
Estrutura Sequencial

Source...: Python Brasil
URL......: https://wiki.python.org.br/EstruturaSequencial
Data.....: 03.07.2022
Estudante: Filipe Azoubel
-------------------------------------------------------------------------
'''

print('\n* * * * Salário * * * *\n')

ganho_por_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = int(input('Digite quantas horas foram trabalhadas: '))
salario_final = ganho_por_hora * horas_trabalhadas

print(f'''
Ganho por hora: R${ganho_por_hora:.2f}
Horas trabalhadas: {horas_trabalhadas}
Salário final: R${salario_final:.2f}
''')

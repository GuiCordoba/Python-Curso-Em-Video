''' Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] < 5:
     aluno['situação'] = 'Reprovado(a)'
elif   5 >=  aluno['media'] < 7:
     aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado(a)'
print('-' * 25)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
salario = int(input('Informe seu salario: '))

if (salario <= 600):
    percentual = 17
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual}%')

elif (salario <= 900):
    percentual = 13
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho:{reajuste:.2f}\nEm percentual: {percentual}%')

elif (salario <= 1500):
    percentual = 12
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho:{reajuste:.2f}\nEm percentual: {percentual}%')

elif (salario <= 2000):
    percentual = 10
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho:{reajuste:.2f}\nEm percentual: {percentual}%')

else:
    percentual = 5
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
    print(f'Novo salario: {novo_salario:.2f}\nReajuste ganho:{reajuste:.2f}\nEm percentual: {percentual}%')
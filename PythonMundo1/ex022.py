nome = str(input('Insira seu nome completo: ')).strip()
div = nome.split()
print('Todas letras maiuscula: {}'.format(nome.upper()))
print('Todas as letras minuscola: {}'.format(nome.lower()))
print('Quantidades de letra: {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome e {} e a quantidades de letras nele e: {}'.format(div[0], len(div[0])))
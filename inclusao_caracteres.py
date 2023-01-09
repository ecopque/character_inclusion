nome = 'Edson Copque'
indice = 0
while indice < len(nome):
    print(nome[indice])
    indice += 1

nome = 'Edson Copque'
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1
print(novo_nome)

nome = 'Edson Copque'
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice] # indice atual do "nome"
    novo_nome += f'*{letra}' # incluindo "*" antes da letra
    indice += 1
novo_nome += '*'
print(novo_nome)
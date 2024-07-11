lista = []

while True:
    a = input('Digite o nome da sua tarefa ou s para sair: ')
    if a.lower() == 's':
        break
    else:
        lista.append(a)

for item in lista:
    print(item.capitalize())
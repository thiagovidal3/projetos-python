from random import randint
numero = randint(1,10)
tentativa = 1

def menu():
    print("""Olá! Seja bem-vindo ao jogo de adivinhação! Sortearemos um número entre 1 e 10 e você terá que adivinhar
    qual o número sorteado, sem limite de tentativas! Para jogar, digite j, ou digite s para sair!
    """)
    while True:

        acao = str(input('Digite sua ação: '))
        if acao == 'j':
            main()
            break
        elif acao == 's':
            print('Você finalizou o jogo com sucesso!')
            break
        else:
            print('Valor inválido!')

def main():

    global tentativa
    while True:
        try:
            palpite = int(input('Digite um número de 1 a 10: '))
            if palpite < 1 or palpite > 10:
                print('Você digitou um número inválido!')
            else:
                if palpite == numero:
                    print(f'Parabéns, você acertou, o número sorteado foi o {numero} e você acertou em {tentativa} tentativa(s)!')
                    break
                elif palpite > numero:
                    print('O número que você chutou é maior do que o número sorteado.')
                    tentativa += 1
                elif palpite < numero:
                    print('O número que você chutou é menor do que o número sorteado')
                    tentativa += 1
        except:
            print('O valor digitado é inválido!')


menu()


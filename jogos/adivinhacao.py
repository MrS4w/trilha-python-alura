import random


def jogar():
    print("*" * 22)
    print("* Jogo de advinhação *")
    print("*" * 22)

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    rodada = 1
    pontos = 100

    print("\nQual nível de dificuldade?")
    print("1 - Fácil\n2 - Médio\n3 - Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas = 15
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f"\nTentativa {rodada} de {total_tentativas}\n")
        rodada += 1
        chute = int(input("Digite um número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print(f"\nVocê digitou: {chute}\n")

        if acertou:
            print(f"Você acertou!\nSeus pontos: {pontos}/100")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto!\n")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto!\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print(f"O número secreto era {numero_secreto}!\n")
    print("*" * 15)
    print("* Fim do jogo *")
    print("*" * 15)


if __name__ == "__main__":
    jogar()

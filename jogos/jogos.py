import forca
import adivinhacao


def escolhe_jogo():
    print("*" * 22)
    print("* Escolha o seu jogo *")
    print("*" * 22)

    print("\n1 - Forca\n2 - Adivinhação\n")

    jogo = int(input("Selecione: "))

    if jogo == 1:
        print("\nJogando forca!\n")
        forca.jogar()
    elif jogo == 2:
        print("\nJogando adivinhação!\n")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()

from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Victor', 8.5)
restaurante_praca.receber_avaliacao('Victor', 4.5)
restaurante_praca.alternar_status()


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()

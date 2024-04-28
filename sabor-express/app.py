import os

restaurantes = []

def exibir_nome():
    print("""
╔═══╗──╔╗───────╔═══╗
║╔═╗║──║║───────║╔══╝
║╚══╦══╣╚═╦══╦═╗║╚══╦╗╔╦══╦═╦══╦══╦══╗
╚══╗║╔╗║╔╗║╔╗║╔╝║╔══╩╬╬╣╔╗║╔╣║═╣══╣══╣
║╚═╝║╔╗║╚╝║╚╝║║─║╚══╦╬╬╣╚╝║║║║═╬══╠══║
╚═══╩╝╚╩══╩══╩╝─╚═══╩╝╚╣╔═╩╝╚══╩══╩══╝
───────────────────────║║
───────────────────────╚╝
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar\Desativar restaurante')
    print('4. Sair\n')
    
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    exibir_subtitulo('Finalizando a aplicação.')
    
def opcao_invalida():
    print('Opção inválida!')
    voltar_menu()
    
def cadastrar_restaurante():
    '''Função responsável por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastro de restaurantes')

    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria':categoria, 'ativo': False}
    
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    
    voltar_menu()

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados: ')
    print(f"{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_menu()

def alterar_estado_restaurante():
    exibir_subtitulo('Alterando estado')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    voltar_menu()

def escolher_opcoes():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()
        
def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
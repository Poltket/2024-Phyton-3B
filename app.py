import os

carros = []

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('')

def retorna_menu_principal():
     input('\n Digite qualquer tecla para voltar ao menu principal')
     main()

def mostra_titulo():
    print("""
            
    ██████╗░██╗░░██╗░█████╗░██████╗░░██████╗
    ██╔══██╗██║░██╔╝██╔══██╗██╔══██╗██╔════╝
    ██████╔╝█████═╝░███████║██████╔╝╚█████╗░
    ██╔══██╗██╔═██╗░██╔══██║██╔══██╗░╚═══██╗
    ██║░░██║██║░╚██╗██║░░██║██║░░██║██████╔╝
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

        """)
    
def mostra_escolha():
    print('1. Cadastro de carros')
    print('2. Listar carros')
    print('3. Ativar carros')
    print('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_carros()
        elif opcao_escolhida == 2:
            mostrar_carros
        elif opcao_escolhida == 3:
            print('Ativar/desativar carro')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()

    except:
         opcao_invalida()

def cadastrar_carros():
    exibir_subtitulo('Cadastrar carros')

    nome_carro = input('Digite o nome do carro: ')
    carros.append(nome_carro)
    print(f'{nome_carro} foi adicionado a lista de carros')
    input('Digite qualquer tecla para voltar')
    main()

def mostrar_carros():
    exibir_subtitulo('Listar carros')
    
    for carro in carros:
         print(f' - carro')

    input('Digite qualquer tecla para voltar')
    main()

def finalizar_programa():
        os. syatem('cls')
        print('Finalizando programa')

def opcao_invalida():
        print('Este caracter não é permitido')
        input('Digite qualquer tecla')
        main()

def main():
    mostra_titulo()
    mostra_escolha()
    escolhe_opcao()

if __name__ == '__main__':
    main()
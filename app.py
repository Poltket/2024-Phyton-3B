import os

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
    opcao_escolhida = int(input('Escolha uma opção: '))
    print('Você escolheu a opção: ', opcao_escolhida)

    def finalizar_programa():
        os. syatem('cls')
        print('Finalizando programa')

    if opcao_escolhida == 1:
        print('Cadastrar carro')
    elif opcao_escolhida == 2:
        print('Listar carro')
    elif opcao_escolhida == 3:
        print('Ativar/desativar carro')
    else:
        finalizar_programa()

def main():
    mostra_titulo()
    mostra_escolha()
    escolhe_opcao()

if __name__ == '__main__':
    main()
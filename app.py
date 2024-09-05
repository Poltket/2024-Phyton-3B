print("""
           
██████╗░██╗░░██╗░█████╗░██████╗░░██████╗
██╔══██╗██║░██╔╝██╔══██╗██╔══██╗██╔════╝
██████╔╝█████═╝░███████║██████╔╝╚█████╗░
██╔══██╗██╔═██╗░██╔══██║██╔══██╗░╚═══██╗
██║░░██║██║░╚██╗██║░░██║██║░░██║██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

      """)
print('1. Cadastro de carros')
print('2. Listar carros')
print('3. Ativar carros')
print('4. Sair da aplicação')

opcao_escolhida = int(input('Escolha uma opção: '))
print('Você escolheu a opção: ', opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar carro')
elif opcao_escolhida == 2:
    print('Listar carro')
elif opcao_escolhida == 3:
    print('Ativar/desativar carro')
else:
    print('Saindo da aplicação')
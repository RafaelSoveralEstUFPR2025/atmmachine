from infra.persistencia import carregar_dados, salvar_dados
from application.servicos import *

def menu():
    print("""
Menu:
1- Cadastrar Conta
2- Visualizar Contas
3- Visualizar Conta
4- Empréstimo
5- Depósito
6- Saque
7- Atualizar Nome
8- Excluir Conta
9- Sair
""")

def main():
    """
    Função principal do programa.

    Carrega os dados do arquivo JSON e exibe um menu para o usuário.
    O usuário pode escolher uma opção do menu e realizar uma ação.
    """
    dados = carregar_dados()
    while True:
        menu()
        opcao = input("Digite uma opção: ")

        if opcao == "1":
            numero = input("Número da conta: ")
            nome = input("Nome do cliente: ")
            saldo = float(input("Saldo inicial: "))
            dados, msg = cadastrar_conta(dados, numero, nome, saldo)
            print(msg)

        elif opcao == "2":
            dados, msg = visualizar_contas(dados)
            if dados:
                for numero, conta in dados.items():
                    print(f"{numero}: {list(conta.values())}")
            else:
                print(msg)

        elif opcao == "3":
            numero = input("Número da conta: ")
            conta, msg = visualizar_conta(dados, numero)
            if conta:
                print(f"{numero}: {list(conta.values())}")
            else:
                print(msg)

        elif opcao == "4":
            numero = input("Número da conta: ")
            valor = float(input("Valor do empréstimo: "))
            confirmar = input("Confirmar empréstimo (s/n)? ").lower()
            if confirmar == "s":
                dados, msg = realizar_emprestimo(dados, numero, valor)
                print(msg)

        elif opcao == "5":
            numero = input("Número da conta: ")
            valor = float(input("Valor do depósito: "))
            dados, msg = realizar_deposito(dados, numero, valor)
            print(msg)

        elif opcao == "6":
            numero = input("Número da conta: ")
            valor = float(input("Valor do saque: "))
            dados, msg = realizar_saque(dados, numero, valor)
            print(msg)

        elif opcao == "7":
            numero = input("Número da conta: ")
            novo_nome = input("Novo nome: ")
            dados, msg = atualizar_nome_conta(dados, numero, novo_nome)
            print(msg)

        elif opcao == "8":
            numero = input("Número da conta: ")
            dados, msg = excluir_conta(dados, numero)
            print(msg)

        elif opcao == "9":
            salvar_dados(dados)
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
from domain.conta import *

def cadastrar_conta(dados, numero, nome, saldo):
    """Cadastra uma nova conta.

    Recebe como parâmetro o dicionário com as contas, o número da conta,
    o nome do cliente e o saldo inicial.
    Se o número da conta ja existir, retorna o dicionário com as contas
    e uma mensagem de erro.
    """
    if numero in dados:
        return dados, "Número de conta já existe."
    conta = criar_conta(numero, nome, saldo)
    dados[numero] = conta
    return dados, "Conta cadastrada com sucesso."

def visualizar_conta(dados, numero):
    """Visualiza uma conta.

    Recebe como parâmetro o dicionário com as contas e o número da conta.
    Se a conta existir, retorna o dicionário com a conta e uma mensagem vazia.
    Se a conta não existir, retorna None e uma mensagem de erro.
    """
    conta = dados.get(numero)
    if conta:
        return conta, ""
    return None, "Conta não encontrada."

def visualizar_contas(dados):
    """Visualiza todas as contas.

    Recebe como parâmetro o dicionário com as contas.
    Retorna o dicionário com as contas e uma mensagem vazia.
    """
    return dados, ""

def realizar_emprestimo(dados, numero, valor):
    """Realiza um empréstimo em uma conta.

    Recebe como parâmetro o dicionário com as contas, o número da conta e o
    valor do empréstimo.
    Se a conta não existir, retorna o dicionário com as contas e uma mensagem
    de erro.
    Se o valor do empréstimo for inválido, retorna o dicionário com as contas
    e uma mensagem de erro.
    Se o empréstimo for realizado com sucesso, retorna o dicionário com as
    contas e uma mensagem de sucesso.
    """
    conta = dados.get(numero)
    if not conta:
        return dados, "Conta não encontrada."
    conta, msg = emprestar(conta, valor)
    dados[numero] = conta
    return dados, msg

def excluir_conta(dados, numero):
    """Exclui uma conta.

    Recebe como parâmetro o dicionário com as contas e o número da conta.
    Se a conta existir, exclui a conta do dicionário e retorna o dicionário
    com as contas e uma mensagem de sucesso.
    Se a conta não existir, retorna o dicionário com as contas e uma mensagem
    de erro.
    """
    if numero in dados:
        del dados[numero]
        return dados, "Conta excluída com sucesso."
    return dados, "Conta não encontrada."

def realizar_deposito(dados, numero, valor):
    """Realiza um depósito em uma conta.

    Recebe como parâmetro o dicionário com as contas, o número da conta e o
    valor do depósito.
    Se a conta não existir, retorna o dicionário com as contas e uma mensagem
    de erro.
    Se o valor do depósito for inválido, retorna o dicionário com as contas
    e uma mensagem de erro.
    Se o depósito for realizado com sucesso, retorna o dicionário com as
    contas e uma mensagem de sucesso.
    """
    conta = dados.get(numero)
    if not conta:
        return dados, "Conta não encontrada."
    conta, msg = depositar(conta, valor)
    dados[numero] = conta
    return dados, msg

def realizar_saque(dados, numero, valor):
    """Realiza um saque em uma conta.

    Recebe como parâmetro o dicionário com as contas, o número da conta e o
    valor do saque.
    Se a conta não existir, retorna o dicionário com as contas e uma mensagem
    de erro.
    Se o valor do saque for inválido, retorna o dicionário com as contas
    e uma mensagem de erro.
    Se o saque for realizado com sucesso, retorna o dicionário com as
    contas e uma mensagem de sucesso.
    """
    conta = dados.get(numero)
    if not conta:
        return dados, "Conta não encontrada."
    conta, msg = sacar(conta, valor)
    dados[numero] = conta
    return dados, msg

def atualizar_nome_conta(dados, numero, novo_nome):
    """Atualiza o nome de uma conta.

    Recebe como parâmetro o dicionário com as contas, o número da conta e o
    novo nome do cliente.
    Se a conta não existir, retorna o dicionário com as contas e uma mensagem
    de erro.
    Se o nome do cliente for inválido, retorna o dicionário com as contas
    e uma mensagem de erro.
    Se o nome do cliente for atualizado com sucesso, retorna o dicionário com
    as contas e uma mensagem de sucesso.
    """
    conta = dados.get(numero)
    if not conta:
        return dados, "Conta não encontrada."
    conta = atualizar_nome(conta, novo_nome)
    dados[numero] = conta
    return dados, "Nome atualizado com sucesso."

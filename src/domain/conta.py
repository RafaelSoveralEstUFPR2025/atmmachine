def criar_conta(numero, nome, saldo_inicial):
    """
    Cria uma conta com os dados informados.

    Args:
        numero (str): Número da conta.
        nome (str): Nome do cliente.
        saldo_inicial (float): Saldo inicial da conta.

    Returns:
        dict: Dicionário com os dados da conta.
    """
    return {
        "numero": numero,
        "nome": nome,
        "saldo": float(saldo_inicial),
        "status": "ativo"
    }

def depositar(conta, valor):
    """
    Realiza um depósito na conta.

    Args:
        conta (dict): Dicionário com os dados da conta.
        valor (float): Valor do depósito.

    Returns:
        tuple: Dicionário com os dados da conta e uma mensagem.
    """
    if valor <= 0:
        return conta, "Valor inválido para depósito."
    conta["saldo"] += valor
    return conta, "Depósito realizado com sucesso."

def sacar(conta, valor):
    """
    Realiza um saque na conta.

    Args:
        conta (dict): Dicionário com os dados da conta.
        valor (float): Valor do saque.

    Returns:
        tuple: Dicionário com os dados da conta e uma mensagem.
    """
    if valor <= 0 or valor > conta["saldo"]:
        return conta, "Saldo insuficiente ou valor inválido."
    conta["saldo"] -= valor
    return conta, "Saque realizado com sucesso."

def emprestar(conta, valor):
    """
    Realiza um empréstimo na conta.

    Args:
        conta (dict): Dicionário com os dados da conta.
        valor (float): Valor do empréstimo.

    Returns:
        tuple: Dicionário com os dados da conta e uma mensagem.
    """
    if valor <= 0:
        return conta, "Valor de empréstimo inválido."
    conta["saldo"] += valor
    return conta, "Empréstimo realizado com sucesso."

def atualizar_nome(conta, novo_nome):
    """
    Atualiza o nome do cliente da conta.

    Args:
        conta (dict): Dicionário com os dados da conta.
        novo_nome (str): Novo nome do cliente.

    Returns:
        dict: Dicionário com os dados da conta.
    """
    conta["nome"] = novo_nome
    return conta
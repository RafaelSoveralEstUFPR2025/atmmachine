import json
import os

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), 'data', 'dados_contas.json')

def carregar_dados():
    """Carrega os dados do arquivo json.

    Se o arquivo não existir, ele é criado e um dicionário vazio é retornado.
    Se o arquivo existir, o seu conteúdo é lido e retornado como um dicionário.
    """
    if not os.path.exists(CAMINHO_ARQUIVO):
        open(CAMINHO_ARQUIVO, "w").close()
        return {}
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    """Salva os dados no arquivo json.

    Recebe um dicionário como parâmetro e salva o seu conteúdo no arquivo.
    """
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)
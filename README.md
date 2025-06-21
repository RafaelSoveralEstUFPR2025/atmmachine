### Como executar o projeto?
1. Clone este repositório
2. Execute o comando
```
python3 src/main.py
```

//DOCUMENTAÇÃO DO PROGRAMA:

# Objetivo do código:
Implementar um programa para simular o funcionamento de um caixa eletrônico (ATM). O sistema deve permitir que o usuário realize operações como visualização de contas cadastradas, empréstimo, saques, depósitos, atualizar nome e excluir conta. Caso o usuário ainda não possua uma conta, o programa também deverá permitir a criação de um novo cadastro.

# Descrição da Lógica:
Foram criados quatro arquivos principais no projeto: main.py, persistencia.py, conta.py e serviços.py.

•	main.py: Contém a função responsável por exibir o menu principal e executar as ações conforme a opção escolhida pelo usuário (de 1 a 9).
•	persistencia.py: Possui duas funções principais: uma para carregar os dados e outra para salvá-los. Os dados são armazenados na pasta data, no arquivo dados_contas.json.
•	conta.py: Implementa as funcionalidades relacionadas à conta bancária, incluindo criação de conta, depósito, saque, solicitação de empréstimo e atualização do nome do cliente.
•	serviços.py: Contém funções auxiliares para executar as funcionalidades definidas no arquivo conta.py.

# Detalhes Relevantes:
Melhorias para o sistema:
•	Será necessário aprimorar a segurança do programa, considerando que atualmente não há cadastro de senha nem autenticação para verificar se a conta realmente pertence ao usuário e se a senha fornecida é válida. 
•	Aprimorar a opção de Visualizar Contas e Visualizar Conta, fazer com que as duas fique uma opção somente.
•	Implementar o tratamento de erros, quando o usuário digitar algum comando errado.

Estrutura de dados utilizada:
•	O projeto utiliza dicionários para representar as contas bancárias, armazenando informações como número da conta, nome do cliente, saldo e status. Essa escolha permite fácil acesso e manipulação dos dados.

Funções modulares:
•	Cada operação bancária (criação da conta, depósito, saque, empréstimo, atualização de nome) foi implementada como uma função separada, facilitando a manutenção, reutilização e testes.

Validações básicas:
•	As funções incluem validações simples, como impedir depósitos ou saques de valores negativos e garantir que o saldo seja suficiente para realizar saques.

Retorno das funções:
•	As funções que modificam o saldo retornam uma tupla com o dicionário atualizado e uma mensagem de status, permitindo feedback claro sobre a operação.

Possível expansão:
•	A arquitetura permite futura inclusão de funcionalidades, como persistência em arquivo, interface gráfica ou tratamento de múltiplas contas em uma lista.
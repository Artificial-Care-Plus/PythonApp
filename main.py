import crud
import validation
import json
import pandas as pd

lista_nome_dados = ["id", "nome", "email", "senha", "nascimento", "peso", "altura"]
lista_nome_dados_dicas = ["id", "categoria", "texto"]

def criarJson(data):
    nome_arquivo = input('Digite o nome do arquivo: ')
    with open(f"{nome_arquivo}.json", 'w') as arquivo:
        json.dump(data, arquivo)

def main():
    print('Bem vindo ao nosso sistema de gerenciamento!')
    while True:
        print('Escolha uma opção:')
        print('1 - Gerenciar Clientes')
        print('2 - Gerenciar Dicas')
        print('3 - Sair')
        # Não colocamos a opção de gerenciar ações pois isso é algo que o admin não deve fazer
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            gerenciarClientes()
        elif opcao == '2':
            gerenciarDicas()
        elif opcao == '3':
            print('Obrigado por usar nosso sistema!')
            break
        else:
            print('Opção inválida!')
            
def gerenciarClientes():
    while True:
        print('Escolha uma opção:')
        print('1 - Listar Clientes')
        print('2 - Listar por Email')
        print('3 - Cadastrar Cliente')
        print('4 - Alterar Cliente')
        print('5 - Excluir Cliente')
        print('6 - Voltar')
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            listarClientes()
        elif opcao == '2':
            listarClientesPorEmail()
        elif opcao == '3':
            cadastrarCliente()
        elif opcao == '4':
            alterarCliente()
        elif opcao == '5':
            excluirCliente()
        elif opcao == '6':
            break
        else:
            print('Opção inválida!')

def listarClientes():
    print('Lista de Clientes:')
    
    lista = crud.selectUsuario()
    # Tratando os dados
    lista_dados = []
    for linha in lista:
        dados = {}
        for i in range(len(linha)):
            dados[lista_nome_dados[i]] = linha[i]
        lista_dados.append(dados)
    # Imprimindo os dados
    print(pd.DataFrame(lista_dados))
    
    print('\nDeseja salvar os dados em um arquivo?')
    if (validation.validarSimNao()):
        # Criar arquivo json com os dados        
        criarJson(lista_dados)
        print('Arquivo salvo com sucesso!\n')
    else:
        print('Ok!\n')

def listarClientesPorEmail():
    print('Lista de Clientes por Email:')
    # Pegando o email do usuário
    print('Digite o email do usuário que deseja listar')
    email = validation.validarEmailSeExiste()
    # Buscando o usuário
    lista_dado = crud.selectUsarioByEmail(email)
    # Tratando os dados
    dados = {}
    for i in range(len(lista_dado[0])):
        dados[lista_nome_dados[i]] = lista_dado[0][i]
    # Imprimindo os dados
    print(pd.DataFrame(dados, index=[0]))
    
    print('\nDeseja salvar os dados em um arquivo?')
    if (validation.validarSimNao()):
        # Criar arquivo json com os dados        
        criarJson(dados)
        print('Arquivo salvo com sucesso!\n')
    else:
        print('Ok!\n')

        
def cadastrarCliente():
    print('Cadastrar Cliente:')
    # Pegando os dados do usuário
    nome = validation.validarNome()
    email = validation.validarEmail()
    senha = validation.validarSenha()
    nascimento = validation.validarNascimento()
    peso = validation.validarPeso()
    altura = validation.validarAltura()
    # Criando o dicionário
    usuario = {"nome": nome, "email": email, "senha": senha, "nascimento": nascimento, "peso": peso, "altura": altura}
    # Salvando no banco de dados
    resultado = crud.createUsuario(usuario)
    print(f'{resultado["mensagem"]}\n')
    
def alterarCliente():
    print('Alterar Cliente:')
    # Pegando o email do usuário
    print('Digite o email do usuário que deseja alterar')
    email = validation.validarEmailSeExiste()
    # Descobrindo se quer alterar o email
    print('Deseja alterar o email desse cliente?')
    if validation.validarSimNao():
        novo_email = validation.validarEmail()
    else:
        novo_email = email
    # Alterando os dados
    print('Digite os novos dados:')
    nome = validation.validarNome()
    senha = validation.validarSenha()
    nascimento = validation.validarNascimento()
    peso = validation.validarPeso()
    altura = validation.validarAltura()
    # Criando o dicionário
    usuario = {"nome": nome, "email": novo_email, "senha": senha, "nascimento": nascimento, "peso": peso, "altura": altura}
    # Salvando no banco de dados
    resultado = crud.updateUsuario(email, usuario)
    print(f'{resultado["mensagem"]}\n')
    
def excluirCliente():
    print('Excluir Cliente:')
    # Pegando o email do usuário
    print('Digite o email do usuário que deseja excluir')
    email = validation.validarEmailSeExiste()
    # Descobrindo se quer excluir o usuário
    lista_dado = crud.selectUsarioByEmail(email)
    dados = {}
    for i in range(len(lista_dado[0])):
        dados[lista_nome_dados[i]] = lista_dado[0][i]
    print(pd.DataFrame(dados, index=[0]))
    
    print('Deseja excluir o usuário?')
    if validation.validarSimNao():
        # Excluindo o usuário
        resultado = crud.deleteUsuario(email)
        print(f'{resultado["mensagem"]}\n')
    else:
        print('Ok!\n')

def gerenciarDicas():
    while True:
        print('Escolha uma opção:')
        print('1 - Listar Dicas')
        print('2 - Listar por Id')
        print('3 - Cadastrar Dica')
        print('4 - Alterar Dica')
        print('5 - Excluir Dica')
        print('6 - Voltar')
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            listarDicas()
        elif opcao == '2':
            listarDicaPorId()
        elif opcao == '3':
            cadastrarDica()
        elif opcao == '4':
            alterarDica()
        elif opcao == '5':
            excluirDica()
        elif opcao == '6':
            break
        else:
            print('Opção inválida!')
            
def listarDicas():
    print('Lista de Dicas:')
    
    lista = crud.selectDicas()
    # Tratando os dados
    lista_dados = []
    for linha in lista:
        dados = {}
        for i in range(len(linha)):
            dados[lista_nome_dados_dicas[i]] = linha[i]
        lista_dados.append(dados)
    # Imprimindo os dados
    print(pd.DataFrame(lista_dados))
    
    print('\nDeseja salvar os dados em um arquivo?')
    if (validation.validarSimNao()):
        # Criar arquivo json com os dados        
        # Nome do arquivo
        criarJson(lista_dados)
        print('Arquivo salvo com sucesso!\n')
    else:
        print('Ok!\n')
        
def listarDicaPorId():
    print('Lista de Dicas por Id:')
    # Pegando o id do usuário
    print('Digite o id da dica que deseja listar')
    id = validation.validarIdSeExiste()
    # Buscando o usuário
    lista_dado = crud.selectDicasPorId(id)
    # Tratando os dados
    dados = {}
    for i in range(len(lista_dado[0])):
        dados[lista_nome_dados_dicas[i]] = lista_dado[0][i]
    # Imprimindo os dados
    print(pd.DataFrame(dados, index=[0]))
    
    print('\nDeseja salvar os dados em um arquivo?')
    if(validation.validarSimNao()):
        # Criar arquivo json com os dados        
        criarJson(dados)
        print('Arquivo salvo com sucesso!\n')
    else:
        print('Ok!\n')
    
def cadastrarDica():
    print('Cadastrar Dica:')
    # Pegando os dados do usuário
    categoria = validation.validarCategoria()
    texto = validation.validarTexto()
    # Criando o dicionário
    dica = {"categoria": categoria, "texto": texto}
    # Salvando no banco de dados
    resultado = crud.createDica(dica)
    print(f'{resultado["mensagem"]}\n')
    
def alterarDica():
    print('Alterar Dica:')
    # Pegando o id da dica
    print('Digite o id da dica que deseja alterar')
    id = validation.validarIdSeExiste()
    # Alterando dados
    print('Digite os novos dados:')
    categoria = validation.validarCategoria()
    texto = validation.validarTexto()
    # Criando o dicionário
    dica = {"categoria": categoria, "texto": texto}
    # Salvando no banco de dados
    resultado = crud.updateDica(id, dica)
    print(f'{resultado["mensagem"]}\n')
    
def excluirDica():
    print('Excluir Dica:')
    # Pegando o id da dica
    print('Digite o id da dica que deseja excluir')
    id = validation.validarIdSeExiste()
    # Descobrindo se quer excluir a dica
    lista_dado = crud.selectDicasPorId(id)
    dados = {}
    for i in range(len(lista_dado[0])):
        dados[lista_nome_dados_dicas[i]] = lista_dado[0][i]
    print(pd.DataFrame(dados, index=[0]))
    
    print('Deseja excluir a dica?')
    if validation.validarSimNao():
        # Excluindo a dica
        resultado = crud.deleteDica(id)
        print(f'{resultado["mensagem"]}\n')
    else:
        print('Ok!\n')
    
main()
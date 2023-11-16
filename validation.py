from datetime import datetime
import crud

def validarSimNao(): 
    while True:
        resposta = input('Digite [s] para sim ou [n] para não: ').lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print('Opção inválida!')
            
def validarNascimento():
    while True:
        data = input('Digite a data de nascimento no formato YYYY-MM-DD: ')
        try:
            datetime.strptime(data, '%Y-%m-%d')
            return data
        except:
            print('Data inválida!')
            
def validarNome():
    while True:
        nome = input('Digite o nome: ')
        if len(nome) < 3:
            print('Nome inválido! (minimo de 3 caracteres)')
        else:
            return nome
def validarEmail():
    while True:
        email = input('Digite o email: ')
        if len(email) < 3:
            print('Email inválido! (minimo de 3 caracteres)')
        elif '@' not in email:
            print('Email inválido! (deve conter o @)')
        elif crud.existeUsuario(email):
           print('Email já cadastrado!') 
        else:
            return email
def validarSenha():
    while True:
        senha = input('Digite a senha: ')
        if len(senha) < 8:
            print('Senha inválida! (minimo de 8 caracteres)')
        else:
            return senha
def validarPeso():
    while True:
        peso = input('Digite o peso: ')
        try:
            peso = float(peso)
            if 10 < peso > 500:
                print('Peso inválido! (entre 10-500 kg)')
            else:
                return peso
        except:
            print('Peso inválido!')
            
def validarAltura():
    while True:
        altura = input('Digite a altura: ')
        try:
            altura = float(altura)
            if altura > 3.0:
                print('Altura inválida! (maximo de 3.0 metros)')
            elif altura < 0.3:
                print('Altura inválida! (minimo de 0.3 metros)')
            else:
                return altura
        except:
            print('Altura inválida!')
def validarEmailSeExiste():
    while True:
        email = input('Digite o email: ')
        if len(email) < 3:
            print('Email inválido! (minimo de 3 caracteres)')
        elif '@' not in email:
            print('Email inválido! (deve conter o @)')
        elif not crud.existeUsuario(email):
           print('Email não cadastrado!') 
        else:
            return email
def validarCategoria():
    while True:
        categoria = input('Digite a categoria: ')
        if len(categoria) < 1:
            print('Categoria inválida! (minimo de 3 caracteres)')
        elif len(categoria) > 10:
            print('Categoria inválida! (maximo de 10 caracteres)')
        else:
            return categoria
def validarTexto():
    while True:
        texto = input('Digite o texto: ')
        if len(texto) < 1:
            print('Texto inválido! (minimo de 3 caracteres)')
        elif len(texto) > 255:
            print('Texto inválido! (maximo de 255 caracteres)')
        else:
            return texto
def validarIdSeExiste():
    while True:
        id = input('Digite o id: ')
        try:
            int(id)
            if not crud.dicaExiste(id):
                print('Id não cadastrado!')
            else:
                return id
        except:
            print('Id inválido!')
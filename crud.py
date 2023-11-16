import cx_Oracle
import json

# Pegando o usuário e senha do arquivo

path = r"C:\Users\leopi\Downloads\CRUD\CRUD\Aula3\login.json"
with open(path, "r") as arquivo:
    dados = json.load(arquivo)

login = dados["user"]
pswd = dados["password"]

# ESQUELETO BANCO DE DADOS #

# Cria conexão com o banco de dados
def connect():
    '''Caso a conexão já esteja feita, retorna a conexão existente. Caso contrário, cria uma nova conexão. Sem isso o programa não funciona'''
    try:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\leopi\Downloads\CRUD\CRUD\instantclient_21_11")
    except:
        pass
    dsn = cx_Oracle.makedsn(host="oracle.fiap.com.br", port=1521, sid="orcl")
    return cx_Oracle.connect(user=login, password=pswd, dsn=dsn)
     
def selectUsuario():
    conn  = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nome, email, senha , TO_CHAR(nascimento, 'YYYY-MM-DD'), peso, altura FROM T_AC_USUARIO")
    linhas = cursor.fetchall()
    
    conn.commit()
    cursor.close()
    conn.close()
   
    return linhas

def selectUsarioByEmail(email):
    conn  = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nome, email, senha , TO_CHAR(nascimento, 'YYYY-MM-DD'), peso, altura FROM T_AC_USUARIO WHERE EMAIL=:valor1", valor1=email)
    linha = cursor.fetchall()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return linha

def existeUsuario(email):
    conn  = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nome, email, senha , TO_CHAR(nascimento, 'YYYY-MM-DD'), peso, altura FROM T_AC_USUARIO WHERE EMAIL=:valor1", valor1=email)
    linha = cursor.fetchall()
    
    if len(linha) == 0:
        return False
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return True
    
def createUsuario(usuario):   
    conn  = connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO T_AC_USUARIO (NOME, EMAIL, SENHA, NASCIMENTO, PESO, ALTURA) VALUES (:valor1, :valor2, :valor3, TO_DATE(:valor4, 'YYYY-MM-DD'), :valor5, :valor6)",  valor1=usuario["nome"], valor2=usuario["email"], valor3=usuario["senha"], valor4=usuario["nascimento"], valor5=usuario["peso"], valor6=usuario["altura"])
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return {"status": False, "mensagem": f"Erro ao criar usuário!\nerro: {e}"}
    
    return {"status": True, "mensagem": "Usuário criado com sucesso!"}

def updateUsuario(email,usuario):
    conn  = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE T_AC_USUARIO SET NOME=:valor1, EMAIL=:valor2, SENHA=:valor3, NASCIMENTO=TO_DATE(:valor4, 'YYYY-MM-DD'), PESO=:valor5, ALTURA=:valor6 WHERE EMAIL=:valor7",  valor1=usuario["nome"], valor2=usuario["email"], valor3=usuario["senha"], valor4=usuario["nascimento"], valor5=usuario["peso"], valor6=usuario["altura"], valor7=email)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return {"status": False, "mensagem": f"Erro ao atualizar usuário!\nerro: {e}"}
    
    return {"status": True, "mensagem": "Usuário atualizado com sucesso!"}

def deleteUsuario(email):
    conn  = connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute(("DELETE FROM T_AC_ACOES WHERE T_AC_ACOES.T_AC_USUARIO_ID = (SELECT T_AC_USUARIO.id FROM T_AC_USUARIO WHERE T_AC_USUARIO.email = :valor1)"), valor1=email)
        cursor.execute("DELETE FROM T_AC_USUARIO WHERE EMAIL=:valor1", valor1=email)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return {"status": False, "mensagem": f"Erro ao deletar usuário!\nerro: {e}"}
    
    return {"status": True, "mensagem": "Usuário deletado com sucesso!"}

def selectDicas():
    conn  = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, categoria, texto FROM T_AC_DICAS")
    linhas = cursor.fetchall()
    
    conn.commit()
    cursor.close()
    conn.close()
   
    return linhas

def selectDicasPorId(id):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, categoria, texto FROM T_AC_DICAS WHERE id=:valor1", valor1=id)
    linha = cursor.fetchall()
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return linha
    
def dicaExiste(id):
    conn  = connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, categoria, texto FROM T_AC_DICAS WHERE id=:valor1", valor1=id)
    linha = cursor.fetchall()
    
    if len(linha) == 0:
        return False
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return True

def createDica(dica):
    conn  = connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO T_AC_DICAS (categoria, texto) VALUES (:valor1, :valor2)", valor1=dica["categoria"], valor2=dica["texto"] )
        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        return {"status": False, "mensagem": f"Erro ao criar dica!\nerro: {e}"}
    
    return {"status": True, "mensagem": "dica criada com sucesso!"}

def updateDica(id,dica):
    conn  = connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute("UPDATE T_AC_DICAS SET categoria=:valor1, texto=:valor2 WHERE id=:valor3", valor1=dica["categoria"], valor2=dica["texto"], valor3=id)
        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        return {"status": False, "mensagem": f"Erro ao atualizar dica!\nerro: {e}"}
    
    return {"status": True, "mensagem": "dica atualizada com sucesso!"}

def deleteDica(id):
    conn  = connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM T_AC_DICAS WHERE id=:valor1", valor1=id)
        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        return {"status": False, "mensagem": f"Erro ao deletar dica!\nerro: {e}"}
    
    return {"status": True, "mensagem": "dica deletada com sucesso!"}
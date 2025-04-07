import mysql.connector

def criarConexao(endereco, usuario, senha, bancodedados):
    try:
        return mysql.connector.connect(
            host=endereco, 
            user=usuario,
            password=senha,
            database=bancodedados
        )
        
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def encerrarConexao(connection):
    if connection:
        connection.close()

def insertNoBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        id = cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Erro ao inserir no banco de dados: {err}")
        connection.rollback()
        return None
    finally:
        cursor.close()
    return id

def listarBancoDados(connection, sql, params=None):
    try:
        cursor = connection.cursor(prepared=True)
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erro ao listar do banco de dados: {err}")
        return []
    finally:
        cursor.close()
    return results

def atualizarBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        linhasAfetadas = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar o banco de dados: {err}")
        connection.rollback()
        return 0
    finally:
        cursor.close()
    return linhasAfetadas

def excluirBancoDados(connection, sql, dados):
    try:
        cursor = connection.cursor(prepared=True)
        cursor.execute(sql, dados)
        connection.commit()
        linhasAfetadas = cursor.rowcount
    except mysql.connector.Error as err:
        print(f"Erro ao excluir do banco de dados: {err}")
        connection.rollback()
        return 0
    finally:
        cursor.close()
    return linhasAfetadas
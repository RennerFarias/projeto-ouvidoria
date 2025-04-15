from database import *

def conectar_banco():
    conexao = criarConexao("localhost", "root", "12345", "sistema_manifestacoes")
    if not conexao:
        print("Não foi possível conectar ao banco de dados!")
        exit()
    return conexao

def exibir_menu():
    print("\n--- SISTEMA DE OUVIDORIA ---")
    print("1. Listagem das Manifestações")
    print("2. Listagem de Manifestações por Tipo")
    print("3. Criar nova manifestação")
    print("4. Exibir quantidade de manifestações")
    print("5. Pesquisar uma manifestação por código")
    print("6. Excluir uma Manifestação pelo Código")
    print("7. Sair do Sistema.")
    return input("Digite a opção: ")

def listar_todas(conexao):
    manifestacoes = listarBancoDados(conexao, "SELECT codigo, tipo, descricao FROM manifestacoes")
    if not manifestacoes:
        print("\nNenhuma manifestação cadastrada!")
    else:
        print("\n--- TODAS AS MANIFESTAÇÕES ---")
        for codigo, tipo, descricao in manifestacoes:
            print(f"Código: {codigo} | Tipo: {tipo}\nDescrição: {descricao}\n")

def listar_por_tipo(conexao):
    print("\nTipos disponíveis:")
    print("1. Reclamação")
    print("2. Elogio")
    print("3. Sugestão")
    
    tipo_opcao = input("Digite o tipo (1-3): ")
    if tipo_opcao not in ["1", "2", "3"]:
        print("Opção inválida!")
        return
        
    tipo = ["Reclamação", "Elogio", "Sugestão"][int(tipo_opcao)-1]
    manifestacoes = listarBancoDados(conexao, 
        "SELECT codigo, tipo, descricao FROM manifestacoes WHERE tipo = %s", (tipo,))
        
    print(f"\n--- {tipo.upper()} ---")
    if not manifestacoes:
        print(f"Nenhuma {tipo.lower()} encontrada!")
    else:
        for codigo, tipo, descricao in manifestacoes:
            print(f"Código: {codigo}\nDescrição: {descricao}\n")

def criar_manifestacao(conexao):
    print("\n--- NOVA MANIFESTAÇÃO ---")
    print("Tipos: 1) Reclamação 2) Elogio 3) Sugestão")
    
    tipo_opcao = input("Escolha o tipo (1-3): ")
    if tipo_opcao not in ["1", "2", "3"]:
        print("Tipo inválido!")
        return
        
    tipo = ["Reclamação", "Elogio", "Sugestão"][int(tipo_opcao)-1]
    descricao = input("Descrição: ").strip()
    
    if not descricao:
        print("Descrição não pode ser vazia!")
        return
        
    codigo = insertNoBancoDados(conexao,
        "INSERT INTO manifestacoes (tipo, descricao) VALUES (%s, %s)",
        (tipo, descricao))
        
    if codigo:
        print(f"Manifestação cadastrada com sucesso! Código: {codigo}")

def mostrar_quantidade(conexao):
    quantidade = listarBancoDados(conexao, "SELECT COUNT(*) FROM manifestacoes")[0][0]
    print(f"\nTotal de manifestações: {quantidade}")

def pesquisar_por_codigo(conexao):
    codigo = input("Digite o código: ")
    if not codigo.isdigit():
        print("Código inválido!")
        return
        
    resultado = listarBancoDados(conexao,
        "SELECT codigo, tipo, descricao FROM manifestacoes WHERE codigo = %s", (codigo,))
        
    if not resultado:
        print("Manifestação não encontrada!")
    else:
        codigo, tipo, descricao = resultado[0]
        print(f"\n--- MANIFESTAÇÃO {codigo} ---")
        print(f"Tipo: {tipo}")
        print(f"Descrição: {descricao}")

def excluir_manifestacao(conexao):
    codigo = input("Digite o código para excluir: ")
    if not codigo.isdigit():
        print("Código inválido!")
        return
        
    linhas = excluirBancoDados(conexao,
        "DELETE FROM manifestacoes WHERE codigo = %s", (codigo,))
        
    if linhas > 0:
        print("Manifestação excluída com sucesso!")
    else:
        print("Manifestação não encontrada!")

def main():
    conexao = conectar_banco()
    
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            listar_todas(conexao)
        elif opcao == "2":
            listar_por_tipo(conexao)
        elif opcao == "3":
            criar_manifestacao(conexao)
        elif opcao == "4":
            mostrar_quantidade(conexao)
        elif opcao == "5":
            pesquisar_por_codigo(conexao)
        elif opcao == "6":
            excluir_manifestacao(conexao)
        elif opcao == "7":
            print("Saindo do sistema...")
            encerrarConexao(conexao)
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

#para resetar o banco de dados, use o seguinte comando: TRUNCATE TABLE manifestacoes;
#link do video explicando o ouvidoria.py: https://youtu.be/UrvyLwzOOmU
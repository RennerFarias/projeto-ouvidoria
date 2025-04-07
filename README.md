# Sistema de Ouvidoria

## 📝 Descrição
Sistema de gerenciamento de manifestações (reclamações, elogios e sugestões) desenvolvido em Python com MySQL.

## 🛠️ Pré-requisitos
- Python 3.x
- MySQL Server
- Biblioteca `mysql-connector-python` (instalável via `pip install mysql-connector-python`)

## 🗄️ Configuração do Banco de Dados

### 1. Criar o banco de dados e tabela
Execute os seguintes comandos no MySQL:

```sql
-- Cria o banco de dados
CREATE DATABASE IF NOT EXISTS sistema_manifestacoes;

-- Seleciona o banco
USE sistema_manifestacoes;

-- Cria a tabela básica
CREATE TABLE IF NOT EXISTS manifestacoes (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL
);

-- Confirmação
SELECT 'Tabela criada com sucesso! Pronto para usar.' AS Mensagem;
```

### 2. Configurar acesso
Edite no arquivo `ouvidoria.py` as credenciais de conexão na função `conectar_banco()`:
```python
conexao = criarConexao("localhost", "root", "12345", "sistema_manifestacoes")
```
Substitua pelos seus dados de usuário e senha do MySQL.

## 🚀 Como Executar
1. Clone o repositório ou copie os arquivos
2. Instale as dependências:
   ```bash
   pip install mysql-connector-python
   ```
3. Execute o programa:
   ```bash
   python ouvidoria.py
   ```

## 🎯 Funcionalidades
- [1] Listar todas as manifestações
- [2] Listar manifestações por tipo (Reclamação/Elogio/Sugestão)
- [3] Criar nova manifestação
- [4] Exibir quantidade de manifestações
- [5] Pesquisar manifestação por código
- [6] Excluir manifestação por código
- [7] Sair do sistema

## 🔄 Resetar Banco de Dados
Para limpar todos os registros (códigos voltam a contar do 1):
```sql
TRUNCATE TABLE manifestacoes;
```

## 📹 Vídeo Explicativo
Assista ao tutorial no YouTube:  
[Explicação do Sistema de Ouvidoria](https://youtu.be/UrvyLwzOOmU)
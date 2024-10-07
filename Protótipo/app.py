from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error
import os

app = Flask(__name__)

# Nome do arquivo do banco de dados
db_file = 'employees.db'

# Função para criar o banco de dados e a tabela
def create_database_and_table():
    # Conecta-se ao banco de dados (ou cria o arquivo se não existir)
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Criar a tabela se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        """)
        conn.commit()
    except Error as e:
        print(f"Erro ao criar banco de dados ou tabela: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

# Chamada da função para criar o banco de dados e a tabela
create_database_and_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar_login', methods=['POST'])
def processar_login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    
    conn = None
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        # Inserir dados no banco
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, senha))
        conn.commit()
        return "Novo registro criado com sucesso"
    except Error as e:
        return f"Erro: {e}"
    finally:
        if conn:
            cursor.close()
            conn.close()

@app.route('/usuarios')
def listar_usuarios():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()  # Busca todos os registros
        return render_template('usuarios.html', usuarios=usuarios)  # Renderiza uma nova página
    except Error as e:
        return f"Erro: {e}"
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)

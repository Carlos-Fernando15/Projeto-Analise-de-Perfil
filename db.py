import sqlite3

def conectar_banco():
    conn = sqlite3.connect('sistema_recrutamento.db')
    return conn

def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()

    # Criação da tabela de candidatos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS candidatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT,
        habilidades TEXT,
        experiencia TEXT,
        formacao TEXT,
        endereco TEXT,
        data_nascimento TEXT,
        objetivo_profissional TEXT,
        idiomas TEXT,
        certificacoes TEXT,
        linkedin TEXT
    )
    ''')

    # Criação da tabela de vagas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vagas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        descricao TEXT,
        requisitos TEXT,
        localizacao TEXT,
        salario TEXT,
        beneficios TEXT
    )
    ''')

    conn.commit()
    conn.close()

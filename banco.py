import sqlite3

def init_db():
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT, valor REAL, data TEXT,
            categoria TEXT, descricao TEXT,
            origem TEXT, nota_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def inserir_transacao(transacao):
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO transacoes (tipo, valor, data, categoria, descricao, origem, nota_path)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        transacao['tipo'], transacao['valor'], transacao['data'],
        transacao['categoria'], transacao['descricao'],
        transacao['origem'], transacao['nota_path']
    ))
    conn.commit()
    conn.close()

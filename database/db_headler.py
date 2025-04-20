import sqlite3
from datetime import datetime

DB_PATH = "payable.db"

def criar_tabela():
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS boletos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            valor REAL NOT NULL,    
            vencimento TEXT NOT NULL,
            motivo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            registrado_em TEXT NOT NULL,
            notificado INTEGER DEFAULT 0  
        )
    ''')

    conn.commit()
    conn.close()

def inserir_boletos(dados):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO boletos (nome, valor, vencimento, motivo, categoria, registrado_em,)
        VALUES (?, ?, ?, ?, ?, ?) 
    ''',(
        dados['nome'],
        dados['valoe'],
        dados['vencimento'],
        dados['motivo'],
        dados['categoria'],
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))

def buscar_boletos_pendentes(dias_para_vencer=3):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id, nome, valor, vencimento FROM boletos
        WHERE notificado = 0
    ''')

    todos = cursor.fetchall()
    conn.close()

    proximos = []
    hoje =  datetime.today()

    for boleto in todos:
        id, nome, valor, venc = boleto

        try:
            venc_date = datetime.strptime(venc, '%d/%m/%Y')
            dias = (venc_date - hoje).days
            if 0 <= dias <= dias_para_vencer:
                proximos.append({
                    'id': id,
                    'nome': nome,
                    'valor': valor,
                    'vencimento': venc
                })
        except:
            continue 
    return proximos

def atualizar_notificacao(id_boleto):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE boletos SET notificado = 1 WHERE id = ?
    ''', (id_boleto,))

    conn.commit()
    conn.close()
    
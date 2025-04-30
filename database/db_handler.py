import mysql.connector
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'kaueodevSQLguim4',
    'database': 'payable'
}

def inserir_boleto(dados):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        sql = '''
            INSERT INTO boletos (nome, valor, vencimento, motivo, categoria, registro)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''

        valores = (
            dados['nome'],
            dados['valor'],
            dados['vencimento'],
            dados['motivo'],
            dados['categoria'],
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        cursor.execute(sql, valores)
        conn.commit()
        print("Boleto salvo com sucesso no MySQL!")

    except mysql.connector.Error as erro:
        print("Erro ao conectar/inserir:", erro)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

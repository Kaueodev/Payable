import mysql.connector
from database.db_handler import DB_CONFIG

def listar_boletos():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, valor, vencimento, motivo, categoria, registro FROM boletos")
        boletos = cursor.fetchall()

        if boletos:

            print('Lista de boletos salvos:')
            for b in boletos:
                print(f"ID: {b[0]}")
                print(f"Nome: {b[1]}")
                print(f"Valor: R${b[2]:.2f}")
                print(f"Vencimento: {b[3]}")
                print(f"Motivo: {b[4]}")
                print(f"Categoria: {b[5]}")
                print(f"Registrado em: {b[6]}")
                print("-" * 40)

        else:
            print('Nenhum boleto encontrado no banco.')
            
    except mysql.connector.Error as erro:
        print('Erro ao buscar boletos:', erro)
        
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    listar_boletos()
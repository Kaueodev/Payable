from extractor.manual_entry import manual_entry
from database.db_handler import inserir_boleto

def main():
    print('\nIniciando o Payable com o MySQL')
    dados = manual_entry()
    inserir_boleto(dados)
    print('\n✅ Boleto salvo com sucesso no banco!')

if __name__ == "__main__":
    main()

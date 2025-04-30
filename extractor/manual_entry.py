def manual_entry():

    print('\n📥 Cadastro manual de boleto:')

    nome = input("Nome do pagador: ").strip()

    while True:
        try:
            valor = float(input('Valor do boleto (ex: 129.90):' ).replace(',','.'))
            break
        except ValueError:
            print('"⚠️ Valor inválido. Tente novamente.')

    vencimento = input('Data de vencimento: ').strip()

    motivos_prontos = {
        "1": ("Água", "Essencial"),
        "2": ("Luz", "Essencial"),
        "3": ("Internet", "Essencial"),
        "4": ("Cartão de crédito", "Variável"),
        "5": ("Lojas", "Variável"),
        "6": ("Assinatura (ex: Netflix)", "Serviços"),
        "7": ("Outro", None)
    }

# K key (numero no dicionario) V valor (categoria no dicionario): Percore o dic motivos prontos
    print('\nEscolha o motivo do boleto: ')
    for k, v in motivos_prontos.items():
        print(f'{k}. {v[0]}')

    while True:
        escolha = input('Digite o número da opção: ').strip()
        if escolha in motivos_prontos:
            motivo, categoria = motivos_prontos[escolha]
            break
        else:
            print('⚠️ Opção inválida. Tente novamente.')

    if escolha == '7':
        motivo = input('Digite o motivo do boleto: ').strip()

        print('Escolha a categoria do gasto: ')
        categorias = {
            "1": "Essencial",
            "2": "Variável",
            "3": "Serviços",
            "4": "Outro"
        }

        for k, v in categorias.items():
            print(f'{k}. {v}')

# Mesma lógica do outro dict que percore categorias e valida a informação do usuario 
        while True:
            cat = input('Digite o número da categoria: ').strip()
            if cat in categorias:
                categoria = categorias[cat]
                break
            else:
                print('⚠️ Categoria inválida. Tente novamente.')

    return {
        "nome": nome,
        "valor": valor,
        "vencimento": vencimento,
        "motivo": motivo,
        "categoria": categoria
    }

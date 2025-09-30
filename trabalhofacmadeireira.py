print("Bem-vindo(a) à madeireira Andre Alvino")

valor_tipo = {
    'PIN': 146.40,
    'PER': 176.20,
    'MOG': 196.90,
    'IPE': 210.10,
    'IMB': 220.70
}
 
def escolha_tipo():           #   <- função que escolhe o tipo de madeira
    while True:
        print("\n-- Escolha o tipo de madeira desejado --")
        print("Tora de Pinho = PIN")
        print("Tora de Peroba = PER")
        print("Tora de Mogno = MOG")
        print("Tora de Ipê = IPE")
        print("Tora de Imbuia = IMB")
        
        tipo = input("Digite o código da madeira: ").upper()

        if tipo in valor_tipo:   # se estiver no dicionário
            return valor_tipo[tipo], tipo
        else:
            print("Opção inválida, tente novamente.")  # saída exigida

def qtd_toras():  #<- função que pede a qtd de toras
    while True:
        try:
            qtd = float(input("Digite a quantidade de material em m³: ")) #<- poderia ter deixado int, mas fica mais legal se puder colocar numeros quebrados

            if qtd > 2000:   #<- obriga o usuario a respeitar o limite de 2000
                print("Não aceitamos pedidos com essa quantidade de toras.")
                continue

            
            if qtd <= 100:
                desconto = 0.0
            elif qtd <= 500:
                desconto = 0.04
            elif qtd <= 1000:
                desconto = 0.09
            else:
                desconto = 0.16

            return qtd, desconto
        
        except ValueError:  #<- caso digite texto
            print("Quantidade inválida ou digitada incorretamente.")

def transporte():
    while True:
        print("\n-- Serviço de transporte --")
        print("1 - Rodoviário (R$1000)")
        print("2 - Ferroviário (R$2000)")
        print("3 - Hidroviário (R$2500)")

        opçao = input("Escolha o tipo de transporte: ")

        if opçao == "1":
            return 1000
        elif opçao == "2":
            return 2000
        elif opçao == "3":
            return 2500
        else:
            print("Opção inválida, escolha 1/2/3.")



valor_madeira, tipo_madeira = escolha_tipo()  #<-tipo de madeira

qtd, desconto = qtd_toras() #<- qtd

valor_transporte = transporte() #<- transporte

subtotal = valor_madeira * qtd
valor_desconto = subtotal * desconto   #<- calculo
total = subtotal - valor_desconto + valor_transporte

# print resumindo pedido
print("\n--- RESUMO DO PEDIDO ---")
print(f"Madeira escolhida: {tipo_madeira} - R$ {valor_madeira}/m³")
print(f"Quantidade: {qtd} m³")
print(f"Desconto: {desconto*100}% (R$ {valor_desconto})")
print(f"Transporte: R$ {valor_transporte}")
print(f"TOTAL A PAGAR: R$ {total}")

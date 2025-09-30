print("Seja bem-vindo(a) à Pizzaria André Alvino")  
print('--- Tamanho \\ Pizza Salgada (PS) \\ Pizza Doce (PD)')
print('---   P     \\     R$ 30.00       \\   R$ 34.00')
print('---   M     \\     R$ 45.00       \\   R$ 48.00') #<--- menu (dificilmente vou usar a barra normal, pq meu teclado n tem)
print('---   G     \\     R$ 60.00       \\   R$ 66.00') 
total = 0 #<--- acumulador  
while True:
    sabor = input("\nEscolha o sabor da sua pizza: \n" 
    "PD = Pizza Doce \n" 
    "PS = Pizza Salgada \n" 
    "0 = Sair\n"
    ": ").upper()
    if sabor == "0":
        break  # <--- encerra
    if sabor not in ['PS', 'PD']:
        print("Sabor inválido tente novamente: ")
        continue  #<---- volta para o inicio
    # Escolha do tamanho
    tamanho = input("Escolha o tamanho da pizza (P/M/G): ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido tente novamente: ")
        continue  #< ----- volta para o inicio
    if sabor == 'PS':  #pedido de pizza salgada
        if tamanho == 'P':
            preço = 30
        elif tamanho == 'M':
            preço = 45
        else:
            preço = 60
    else:  #pedido de pizza doce
        if tamanho == 'P':
            preço = 34
        elif tamanho == 'M':
            preço = 48
        else:
            preço = 66
    #atualiza o preço
    total += preço  
    print("Sua pizza {}, tamanho {}, foi adicionada por R$ {:.2f}".format(sabor, tamanho, preço))
    print("Valor parcial do pedido: R$ {:.2f}".format(total)) #2f é para pegar 2 casas decimais, ex: R$ 2,00 
    
    mais = input("Deseja pedir mais alguma coisa? (S\\N): ").upper() #tive que colocar \\ pq fica dando erro
    if mais == "S": #<--- #se o usuario quiser continuar pedindo
        continue  # continua o pedido
    else:
        break  #encerra se não quiser continuar
print("\nPedido encerrado.")
print("O valor total do pedido foi: R$ {:.2f}".format(total))


    

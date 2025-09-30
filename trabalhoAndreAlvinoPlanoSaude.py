print("SEJA BEM-VINDO Á ANDRE ALVINO PLANOS DE SAÚDE")


idade = int(input("Digite sua idade: "))
valorBase = int(input("Digite o valor base de seu plano: "))

if idade >= 0 and idade < 19:
    valorMensal = valorBase * (100 / 100) # <---- calculo do valor mensal igual o do enunciado
    print("O valor mensal do seu plano é de: R$ {}".format(valorMensal)) # <----- .format() para colocar o valor já calculado no print
elif idade >= 19 and idade < 29:
    valorMensal = valorBase * (150 / 100)
    print("O valor mensal do seu plano é de: R$ {}".format(valorMensal))
elif idade >=29 and idade <39:
    valorMensal = valorBase * (225 / 100)
    print("O valor mensal do seu plano é de: R$ {}".format(valorMensal))    
elif idade >= 39 and idade < 49:
    valorMensal = valorBase * (240 / 100)
    print("O valor mensal do seu plano é de: R$ {}".format(valorMensal))
elif idade >= 49 and idade < 59:
    valorMensal = valorBase * (350 / 100)
    print("O valor mensal do seu plano é de: R$ {}".format(valorMensal))
elif idade >= 59:
    valorMensal = valorBase * (600 / 100)
    print("O valor mensal do seu plano é de: R$ {}".format(valorMensal))
else:
    print("Valor inválido, tente novamente!") # <----- se o usuario digitar um valor que não seja inteiro
                                    
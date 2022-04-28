print("                                                     \n")

print("** \033[1;33mMARMITAS GOLDEN / DELIVERY\033[1;m **   \n")

escolha = False
while escolha == False:
    Marmita = input("\033[33mESCOLHA SUA MARMITA: \n\033[m 1- Pequena - R$ 15,00\n 2- Média - R$ 17,00\n 3- Grande - R$ 20,00\n\033[31m Digite o número da opção escolhida: \033[m")
    if (Marmita == "1"):
        escolha = True
        print(" Você escolheu a marmita Pequena - R$ 15,00")
        a = 15
    elif (Marmita == "2"):
        escolha = True
        print(" Você escolheu a marmita Média - R$ 17,00")
        a = 17
    elif (Marmita == "3"):
        escolha = True
        print(" Você escolheu a marmita Grande - R$ 20,00")
        a = 20
    elif ValueError:
        print("                                                     ")
        print(" Opção inválida. Escolha novamente.")
        print("                                                     ")

print("\n============================================== \n")

escolha = False
while escolha == False:
    Menu = input("\033[33mESCOLHA O CARDÁPIO DO DIA: \n\033[m 1- Arroz, Feijão, Farofa e Frango\n 2- Arroz, Feijão, Farofa e Bisteca\n 3- Arroz, Feijão, Farofa e Peixe\n\033[31m Digite o número da opção escolhida: \033[m")
    if (Menu == "1"):
        escolha = True
        print(' Você escolheu a opção: Arroz, Feijão, Farofa e Frango! \n Subtotal: R$ ' + str(a) + ',00 ')
    elif (Menu == "2"):
        escolha = True
        print(' Você escolheu a opção: Arroz, Feijão, Farofa e Bisteca! \n Subtotal: R$ ' + str(a) + ',00 ')
    elif (Menu == "3"):
        escolha = True
        print(' Você escolheu a opção: Arroz, Feijão, Farofa e Peixe! \n Subtotal: R$ ' + str(a) + ',00 ')
    elif ValueError:
        print("                                                     ")
        print(" Opção inválida. Escolha novamente.")
        print("                                                     ")

print("\n============================================== \n")

escolha = False
while escolha == False:
    Bebida = input("\033[33mESCOLHA SUA BEBIDA: \n\033[m 1- Coca-Cola Lata - R$ 6,00 \n 2- Coca-Cola 2 Litros - R$ 10,00 \n 3- Suco de Laranja - R$ 7,00 \n 4- Água sem gás - R$ 3,00 \n 5- Água com gás - R$ 6,00 \n 6- Nenhuma \n\033[31m Digite o número da opção escolhida: \033[m")
    if (Bebida == "1"):
        escolha = True
        b = 6
        print(' Você adicionou: Coca-Cola Lata! \n Subtotal: R$ ' + str(a + b) + ',00 ')
    elif (Bebida == "2"):
        escolha = True
        b = 10
        print(' Você adicionou: Coca-Cola 2 Litros! \n Subtotal: R$ ' + str(a + b) + ',00 ')
    elif (Bebida == "3"):
        escolha = True
        b = 7
        print(' Você adicionou: Suco de Laranja! \n Subtotal: R$ ' + str(a + b) + ',00 ')
    elif (Bebida == "4"):
        escolha = True
        b = 3
        print(' Você adicionou: Água sem gás! \n Subtotal: R$ ' + str(a + b) + ',00 ')
    elif (Bebida == "5"):
        escolha = True
        b = 6
        print(' Você adicionou: Água com gás! \n Subtotal: R$ ' + str(a + b) + ',00 ')
    elif (Bebida == "6"):
        escolha = True
        b = 0
        print(' Você optou por não pedir bebida! \n Subtotal: R$ ' + str(a + b) + ',00 ')
    elif ValueError:
        print("                                                     ")
        print(" Opção inválida. Escolha novamente.")
        print("                                                     ")

print("\n============================================== \n")

Nome = input(f"\033[31m Digite seu nome: \033[m")

Telefone = input("\033[31m Digite seu telefone com DDD: \033[m")

print("\n============================================== \n")

escolha = False
while escolha == False:
    Entrega = input("\033[33mSEU PEDIDO SERÁ: \n\033[m 1- Para entrega \n 2- Retirar no local \n\033[31m Digite o número da opção escolhida: \033[m")
    if (Entrega == "1"):
        escolha = True
        print(' Você optou por realizarmos a entrega!')
        Endereco = int(input("\033[31m Digite seu CEP: \033[m"))
        if (Endereco < 11111111):
            c = 3
            print(' Valor do frete: R$ 3,00!\n Subtotal: R$ ' + str(a + b + c) + ',00 ')
            print("\n============================================== \n")
            rua = str(input("\033[33mCADASTRE SEU ENDEREÇO COMPLETO!\n\033[31mEXEMPLO: RUA, Nº, BAIRRO, CIDADE: \033[m"))
            print("\n============================================== \n")
            escolha = False
            while escolha == False:
                forma = input("\033[33mEFETUAR O PAGAMENTO PELO APLICATIVO OU NA ENTREGA: \n\033[m 1- Aplicativo\n 2- Entrega \n\033[31m Digite o número da opção escolhida: \033[m")
                if (forma == "1"):
                    escolha = True
                    print("Você optou: Pagamento pelo Aplicativo!")
                    print("\n============================================== \n")
                    escolha = False
                    while escolha == False:
                        Pagamento = input("\033[33mESCOLHA A FORMA DE PAGAMENTO: \n\033[m 1- Cartão\n 2- Pix \n\033[31m Digite o número da opção escolhida: \033[m")
                        if (Pagamento == "1"):
                            escolha = True
                            print(" Você escolheu a forma de pagamento: Cartão!")
                            cartão = input("\033[31m Digite o número do cartão: \033[m")
                            print(f" Confirmando o nome do cartão: {cartão}")
                            NomeNocartao = input(f"\033[31m Digite o nome do titular conforme está no cartão: \033[m")
                            print(f" Confirmando o nome do cartão: {NomeNocartao}")
                            codigo = input("\033[31m Digite o código de segurança: \033[m")
                            print(f" Confirmando o código de segurança: {codigo}")
                            print("\n============================================== \n")
                            print("\033[33mNOTA FISCAL:\033[m")
                            print(f" Valor da marmita: R$ {a},00 ")
                            print(f" Valor da bebida: R$ {b},00 ")
                            print(f" Valor do frete: R$ {c},00 ")
                            print("\033[33m Valor total do pedido: R$ " + str(a + b + c) + ',00\033[m')
                            print("\n============================================== \n")
                        elif (Pagamento == "2"):
                            escolha = True
                            print(" Você escolheu a forma de pagamento: Pix! \n Nossa chave pix CNPJ: 34.735.360/0001-70")
                            print("\n============================================== \n")
                            print("\033[33mNOTA FISCAL:\033[m")
                            print(f" Valor da marmita: R$ {a},00 ")
                            print(f" Valor da bebida: R$ {b},00 ")
                            print(f" Valor do frete: R$ {c},00 ")
                            print("\033[33m Valor total do pedido: R$ " + str(a + b + c) + ',00\033[m')
                            print("\n============================================== \n")
                        elif ValueError:
                            print("                                                     ")
                            print(" Opção inválida. Escolha novamente.")
                            print("                                                     ")
                elif (forma == "2"):
                    escolha = True
                    print(" Você escolheu a forma de pagamento: Na entrega!")
                    print("\n============================================== \n")
                    print("\033[33mNOTA FISCAL:\033[m")
                    print(f" Valor da marmita: R$ {a},00 ")
                    print(f" Valor da bebida: R$ {b},00 ")
                    print(f" Valor do frete: R$ {c},00 ")
                    print("\033[33m Valor total do pedido: R$ " + str(a + b + c) + ',00\033[m')
                    print("\n============================================== \n")
                elif ValueError:
                    print("                                                     ")
                    print(" Opção inválida. Escolha novamente.")
                    print("                                                     ")
        elif (Endereco > 11111111):
            c = 6
            print(' Valor do frete: R$ 6,00!\n SUBTOTAL: R$ ' + str(a + b + c) + ',00 ')
            print("\n============================================== \n")
            rua = str(input("\033[33mCADASTRE SEU ENDEREÇO COMPLETO!\n\033[31mEXEMPLO: RUA, Nº, BAIRRO, CIDADE: \033[m"))
            print("\n============================================== \n")
            escolha = False
            while escolha == False:
                forma = input("\033[33mEFETUAR O PAGAMENTO PELO APLICATIVO OU NA ENTREGA: \n\033[m 1- Aplicativo\n 2- Entrega \n\033[31m Digite o número da opção escolhida: \033[m")
                if (forma == "1"):
                    escolha = True
                    print(" Você optou: Pagamento pelo Aplicativo!")
                    print("\n============================================== \n")
                    escolha = False
                    while escolha == False:
                        Pagamento = input("\033[33mESCOLHA A FORMA DE PAGAMENTO: \n\033[m 1- Cartão\n 2- Pix \n\033[31m Digite o número da opção escolhida: \033[m")
                        if (Pagamento == "1"):
                            escolha = True
                            print(" Você escolheu a forma de pagamento: Cartão!")
                            cartão = input("\033[31m Digite o número do cartão: \033[m")
                            print(f" Confirmando o nome do cartão: {cartão}")
                            NomeNocartao = input(f"\033[31m Digite o nome do titular conforme está no cartão: \033[m")
                            print(f" Confirmando o nome do cartão: {NomeNocartao}")
                            codigo = input("\033[31m Digite o código de segurança: \033[m")
                            print(f" Confirmando o código de segurança: {codigo}")
                            print("\n============================================== \n")
                            print("\033[33mNOTA FISCAL:\033[m")
                            print(f" Valor da marmita: R$ {a},00 ")
                            print(f" Valor da bebida: R$ {b},00 ")
                            print(f" Valor do frete: R$ {c},00 ")
                            print("\033[33m Valor total do pedido: R$ " + str(a + b + c) + ',00\033[m')
                            print("\n============================================== \n")
                        elif (Pagamento == "2"):
                            escolha = True
                            print(" Você escolheu a forma de pagamento: Pix! \n Nossa chave pix CNPJ: 34.735.360/0001-70")
                            print("\n============================================== \n")
                            print("\033[33mNOTA FISCAL:\033[m")
                            print(f" Valor da bebida: R$ {b},00 ")
                            print(f" Valor do frete: R$ {c},00 ")
                            print("\033[33m Valor total do pedido: R$ " + str(a + b + c) + ',00\033[m')
                            print("\n============================================== \n")
                        elif ValueError:
                            print("                                                     ")
                            print(" Opção inválida. Escolha novamente.")
                            print("                                                     ")
                elif (forma == "2"):
                    escolha = True
                    print("Você escolheu a forma de pagamento: Na entrega!")
                    print("\n============================================== \n")
                    print("\033[33mNOTA FISCAL:\033[m")
                    print(f" Valor da marmita: R$ {a},00 ")
                    print(f" Valor da bebida: R$ {b},00 ")
                    print(f" Valor do frete: R$ {c},00 ")
                    print("\033[33m Valor total do pedido: R$ " + str(a + b + c) + ',00\033[m' )
                    print("\n============================================== \n")
                elif ValueError:
                    print("                                                     ")
                    print(" Opção inválida. Escolha novamente.")
                    print("                                                     ")
    elif (Entrega == "2"):
            escolha = True
            print(' Você optou por: Retirar no local!')
            print("\n============================================== \n")
            print("\033[33mNOTA FISCAL:\033[m")
            print(f" Valor da marmita: R$ {a},00 ")
            print(f" Valor da bebida: R$ {b},00 ")
            print("\033[33m Valor total do pedido: R$" +str(a + b) + ",00\033[m" )
            print("\n============================================== \n")
    elif ValueError:
        print("                                                     ")
        print(" Opção inválida. Escolha novamente.")
        print("                                                     ")

escolha = False
while escolha == False:
    cpf = input("\033[33mDESEJA CADASTRAR O CPF NA NOTA?\033[m \n 1- Sim\n 2- Não \n\033[31m Digite o número da opção escolhida: \033[m")
    if (cpf == "1"):
        escolha = True
        print(" Você escolheu a opção: Cadastrar CPF!")
        dados = input("\033[31m Digite seu CPF: \033[m")
        print(f" CPF: {dados} cadastrado com sucesso!")
    elif (cpf == "2"):
        escolha = True
        print(" Você escolheu a opção: Não cadastrar CPF!")
    elif ValueError:
        print("                                                     ")
        print(" Opção inválida. Escolha novamente.")
        print("                                                     ")



print("\n============================================== \n")

import random
aleatorio = random.randint(100000, 10000000000)
escolha = False
while escolha == False:
    confirmar = input("\033[33mVOCÊ CONFIRMA SEU PEDIDO:\033[m \n 1- Sim\n 2- Não \n\033[31m Digite o número da opção escolhida: \033[m")
    if (confirmar == "1"):
        escolha = True
        print("\n============================================== \n")
        print(f" Seu pedido foi gerado com sucesso! \n Código do pedido \033[31m{aleatorio}\033[m \n O tempo de preparo e entrega da sua marmita é de 40 minutos! Obrigado(a) {Nome}, volte sempre!")
    elif (confirmar == "2"):
        escolha = True
        print("\n============================================== \n")
        print(" Seu pedido foi cancelado com sucesso!")
    elif ValueError:
        print("                                                     ")
        print(" Opção inválida. Escolha novamente.")
        print("                                                     ")
print("                             \n")

print("** \033[1;33mMARMITAS GOLDEN / DELIVERY\033[1;m **   \n")


print("Curso: Engenharia de Software.")
print("Integrantes que realizaram o projeto: \nBianca Alves Palamar \nGabriel Neri e Costa \nOrlando Eduardo Pereira")





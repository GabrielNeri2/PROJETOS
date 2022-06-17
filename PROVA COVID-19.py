#CABEÇALHO
def imprimir(msg):
    print()
    print('=' * 64)
    print(f'{msg:^64}')
    print('=' * 64)
    print()


imprimir("SEJA BEM-VINDO")


class Cadastro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def pessoa(self):
        print("Seu nome é "+self.nome+"!")

    def numero(self):
        print("Sua idade "+self.idade+" anos!")


class Menu(Cadastro):
    def __init__(self, jogo, sintomas, dados, nome, idade):
        super().__init__(nome, idade)
        self.jogo = jogo
        self.sintomas = sintomas
        self.dados = dados

    def game(self):
        score = 0
        print("Bem-vindo ao Quiz "+self.nome+"! Confirmando sua idade: "+self.idade+" anos!")
        print("******************************")
        print("Responda as perguntas e ganhe um ponto a cada acerto!")

        #PERGUNTA1
        print("Quais são os sintomas do Covid-19? \n (a) Febre, dor de cabeça e tosse \n (b) Dores de ouvido   \n (c) Problemas de visão  \n (d) Nenhum sintoma \n")
        res1 = input("Resposta: ")

        if res1 == "a":
            print("Correto!")
            score = score + 1
        else:
            print("Incorreto!")

        #PERGUNTA2
        print("Meu animal doméstico pode transmitir Covid-19? \n (a) Todos os animais domésticos podem transmitir Covid-19 \n (b) Somente gatos transmitem Covid-19 \n (c) Não há evidências comprovadas que animais domésticos transmitem Covid-19 \n (d) Somente cachorros transmitem Covid-19 \n")
        res2 = input("Resposta: ")

        if res2 == "c":
            print("Correto!")
            score = score + 1
        else:
            print("Incorreto!")

        #PERGUNTA3
        print("Tenho sintomas do Covid-19, posso aglomerar? \n (a) Pode ir somente em lugares fechados \n (b) Pode ir em todos os lugares \n (c) Em caso de sintomas, fique em casa \n (d) Todas estão corretas \n")
        res3 = input("Resposta: ")

        if res3 == "c":
            print("Correto!")
            score = score + 1
        else:
            print("Incorreto!")

        #PERGUNTA4
        print("Tenho uma doença crônica, devo evitar ir aos hospitais para não contrair Covid-19?\n (a) Está liberado frequentar hospitais \n (b) Somente hospitais particulares \n (c) Somente hospitais públicos \n (d) Faça um esforço para evitar hospitais em caso de doença crônica \n")
        res4 = input("Resposta: ")

        if res4 == "d":
            print("Correto!")
            score = score + 1
        else:
            print("Incorreto!")

        #PERGUNTA5
        print("Como devo me preparar na pandemia com relação a suprimentos? \n (a) Verificar se você tem suprimentos como comidas e remédios para algumas semanas  \n (b) Não adquirir suprimentos \n (c) Somente comida como suprimentos, remédios não precisa\n (d) Nenhuma está correta \n")
        res5 = input("Resposta: ")

        if res5 == "a":
            print("Correto!")
            score = score + 1
        else:
            print("Incorreto!")

        if score == 5:
            print(f"Quiz acabou... Pontuação: {score}/5 Parabéns! Você está atualizado sobre a pandemia do Covid-19!")
        else:
            print(f"Quiz acabou... Pontuação: {score}/5 Se Oriente! Covid-19 é sério! Convido você a saber mais sobre como se prevenir contra o Covid-19 no site: https://hc.unicamp.br/coronavirus-covid-19-orientacoes-gerais-para-pacientes-e-populacao-em-geral/ ")

    def amostra(self):
        pontos = 0
        print("Bem-vindo "+self.nome+"! Confirmando sua idade: "+self.idade+" anos!")
        print("******************************")
        print("Responda os sintomas!")

        #PERGUNTA1
        print("Você está com febre e dores de cabeça? \n (a) Sim \n (b) Não")
        res6 = input("Resposta: ")

        if res6 == "a":
            print("Próxima pergunta!")
            pontos = pontos + 1
        else:
            print("Próxima pergunta!")

        #PERGUNTA2
        print("Você está sentindo falta de ar? \n (a) Sim \n (b) Não")
        res7 = input("Resposta: ")

        if res7 == "a":
            print("Próxima pergunta!")
            pontos = pontos + 1
        else:
            print("Próxima pergunta!")

        #PERGUNTA3
        print("Você está com dores de garganta e tosse? \n (a) Sim \n (b) Não")
        res8 = input("Resposta: ")

        if res8 == "a":
            print("Próxima pergunta!")
            pontos = pontos + 1
        else:
            print("Próxima pergunta!")

        #PERGUNTA4
        print("Você teve contato com alguma pessoa com Covid-19? \n (a) Sim \n (b) Não")
        res9 = input("Resposta: ")

        if res9 == "a":
            print("Fim!")
            pontos = pontos + 1
        else:
            print("Fim!")

        if pontos == 0:
            print("Você não tem nenhum sintoma do Covid-19!")

        elif pontos == 1:
            print("Cuide-se! Se previna contra o Covid-19!")

        elif pontos == 2:
            print("Fique em casa! Se previna contra o Covid-19!")

        elif pontos == 3:
            print("Faça o teste do Covid-19!")

        elif pontos == 4:
            print("Faça o teste do Covid-19!")

    def informacoes(self):
        print("Bem-vindo "+self.nome+"! Confirmando sua idade: "+self.idade+" anos!")
        print("******************************")
        print("ORIENTAÇÕES COVID-19:")
        print(''' 
        - Caso não se sinta muito bem, dor de garganta, febre baixa ou tosse, sintomas não intensos, fique em casa!
        - Quando for lavar as mãos, pelo menos 20 segundos com frequência.
        - Ao espirrar ou tossir, cubra o nariz e a boca! Utilize lenço ou papel toalha.
        - Evite lugares aglomerados, com muitas pessoas.
        - Evite contato com pessoas que já estão doentes, mantenha distância e não faça visitas!
        - Em caso de sintomas, evite tocar olhos e nariz.
        - Em caso de febre alta, tosse ou dificuldade para respirar, procure um atendimento hospitalar para fazer o teste do Covid-19! Vá de máscara!
        ''')


id = input("Qual o seu nome? ")
cad = input("Qual a sua idade? ")
humano = Cadastro(id, cad)
humano.pessoa()
humano.numero()
user = Menu("!", "!", "!", id, cad)


#MENU
def escolha():
    while True:
        print("******************************")
        print("ESCOLHA UMA DAS OPÇÕES: ")
        print("1- Quiz Covid-19")
        print("2- Informar sintomas do Covid-19")
        print("3- Orientações para tratamento Covid-19")
        print("4- Sair do programa")
        opcao = input("Qual a sua opção? ")
        print("******************************")

        if opcao == "1":
            user.game()

        elif opcao == "2":
            user.amostra()

        elif opcao == "3":
            user.informacoes()

        elif opcao == "4":
            quit("Você saiu do programa...")

        else:
            print("Opção Inválida!")
            escolha()


escolha()


#FONTE: https://hc.unicamp.br/coronavirus-covid-19-orientacoes-gerais-para-pacientes-e-populacao-em-geral/
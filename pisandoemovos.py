from re import S


jogo = {"Armador": "" ,"Andarilho": "", "1": 0, "2": 0}


campo = [[0, 1, 2, 3, 4, 5, 6, 7], [1, "A", "A", "A", "A", "A", "A", "A"], [2, "A", "A", "A", "A", "A", "A", "A"], [3, "A", "A", "A", "A", "A", "A", "A"], [4, "A", "A", "A", "A", "A", "A", "A"], [5, "A", "A", "A", "A", "A", "A", "A"], [6, "A", "A", "A", "A", "A", "A", "A"], [7, "A", "A", "A", "A", "A", "A", "A"]]

print("\nBem vindo ao jogo: Pisando em Ovos \n")
print("Selecione uma das opções abaixo para iniciar sua aventura:")

def redefinirCampo():
    campobase = [[0, 1, 2, 3, 4, 5, 6, 7], [1, "A", "A", "A", "A", "A", "A", "A"], [2, "A", "A", "A", "A", "A", "A", "A"], [3, "A", "A", "A", "A", "A", "A", "A"], [4, "A", "A", "A", "A", "A", "A", "A"], [5, "A", "A", "A", "A", "A", "A", "A"], [6, "A", "A", "A", "A", "A", "A", "A"], [7, "A", "A", "A", "A", "A", "A", "A"]]
    for j in range(0,7):
        for k in range(0,7):
            campo[j][k] = campobase[j][k]

def menu():
    print("\n1 - Definir Armador \n2 - Plantar Armadilhas \n3 - Iniciar com Andarilho \n4 - Mostrar o placar \n0 - Finalizar o Jogo")

    opcao = int(input())

    if opcao == 1:

        armador = 0
        while armador < 1 or armador > 2:
            print("\nQual jogador plantará as armadilhas? [1 ou 2]")
            armador = int(input())

            if armador == 1:
                print("\nO armador é o jogador: 1\nO andarilho é o jogador: 2")
                jogo["Armador"] = "1"
                jogo["Andarilho"] = "2"
                return menu()

            elif armador == 2:
                print("\nO armador é o jogador: 2\nO andarilho é o jogador: 1")
                jogo["Armador"] = "2"
                jogo["Andarilho"] = "1"
                return menu()

            else:
                print("\nInsira uma das opções válidas.")
                return menu()

    elif opcao == 2:   
        if jogo["Andarilho"] != "1" and jogo["Andarilho"] != "2":
            print("\nEscolha os papéis dos jogadores primeiro.")
            return menu()
            
        else:
            print()
            for l in range(0,8):
                for c in range(0,8):
                    print(campo[l][c],end = " ")
                print()
            print("Jogador {}, você pode esconder até 3 ovos podres por linha do terreno".format(jogo["Armador"]))
            

            def montarCampo():
                totalovos = 0
                cont = 1
                while totalovos < 15 and cont != 8:
                    ovoslinha = 0
                    print("Deseja colocar algum ovo na linha {}? (s/n)".format(cont))
                    resposta = input()
                

                    while resposta != "s" and resposta != "n":
                        print("Insira uma resposta válida. (s/n)" )
                        resposta = input()
                    
                    while resposta == "s" and ovoslinha <= 3:
                        
                        ovoslinha = ovoslinha + 1
                        
                        print("Em qual coluna da linha {} você quer esconder ovos podres? [1 a 7]".format(cont))

                        coluna = int(input())

                        while coluna < 1 and coluna > 7:
                            print("Insira uma resposta válida. (1-7)") 
                            coluna = int(input())

                        while campo[cont][coluna] == "O":
                            print("Insira um casa válida.")
                            coluna = input()


                        campo[cont][coluna] = "O"
                            
                        totalovos = totalovos + 1                       
                            
                        

                        while resposta == "s":
                            print("Gostaria de continuar nessa linha? (s/n)")
                            resposta = input()
                            if resposta == "s":
                                ovoslinha = ovoslinha + 1

                                if ovoslinha < 4:

                                    print("Em qual coluna da linha {}? [1 a 7]".format(cont))

                                    coluna = int(input())

                                    while coluna < 1 or coluna > 7:
                                        print("Insira uma resposta válida.") 
                                        coluna = int(input())

                                    while campo[cont][coluna] == "O":
                                        print("Essa posição já possui ovos.")
                                        print("Insira outra posição.")
                                        coluna = int(input())


                                    campo[cont][coluna] = "O"
                                        
                                    totalovos = totalovos + 1
                                    
                                else:
                                    print("Limite de ovos na linha alcançado.")

                            elif resposta == "n":
                                a = 1
                    
                    if resposta == "n":
                        cont = cont + 1

                    else:
                        print("Insira um valor válido.")

                    
            
                
            
                for l in range(0,8):
                    for c in range(0,8):
                        print(campo[l][c],end = " ")
                    print()
                print("Deseja redefinir o terreno ou manter? (r/m)")
                terreno = input()

                while terreno != "r" and terreno != "m":
                    print("Insira uma resposta válida. (r/m)")
                    terreno = input()

                if terreno == "r":
                    redefinirCampo()
                    montarCampo()

                while terreno == "m":

                    menu()

            montarCampo()

    elif opcao == 3:
        for i in range(1,100):
            for j in range (i):
                print("=", end="")
            print()
        print("São válidos os espaços: [1, 2, 3, 4, 5, 6, 7]\nEscolha sabiamente um dos espaços válidos")
        def andarCasa():
            casa = int(input())
            for t in range(1,7):
                if campo[t][casa] == "O":
                    print("Eca! Você pisou em um ovo podre e perdeu.")
                    jogo[jogo['Armador']] = jogo[jogo['Armador']] + 1
                    redefinirCampo()
                    menu()

                    

                else:
                    esquerda = casa-1
                    direita = casa+1
                    baixo = casa
                    if casa == 1:
                        print("Os espaços disponiveis são: {} e {}".format(baixo,direita))
                        casa = int(input())
                        while casa != baixo and casa != direita:
                            print("Insira uma casa válida.")
                            casa = int(input())
                    elif casa == 7:
                        print("Os espaços disponiveis são: {} e {}".format(esquerda,baixo))
                        casa = int(input())
                        while casa != baixo and casa != esquerda:
                            print("Insira uma casa válida.")
                            casa = int(input())
                    elif casa < 1 or casa > 7:
                        while casa < 1 or casa > 7:
                            print("Insira uma casa válida.")
                            casa = int(input())
                    else:
                        print("Os espaços disponiveis são: {}, {} e {}".format(esquerda,baixo,direita))
                        casa = int(input())
                        while casa != baixo and casa != direita and casa != esquerda:
                            print("Insira uma casa válida.")
                            casa = int(input())

               
            jogo[jogo['Andarilho']] = jogo[jogo['Andarilho']] +1
            print("Você atravessou o terreno sem cair em nenhuma armadilha! Parabéns!!!!")
            redefinirCampo()
            menu()


            
            
        andarCasa()

    elif opcao == 4:    
        print("\nPontuação do jogador 1: {}\nPontuação do jogador 2: {}".format(jogo["1"], jogo["2"]))
        menu()

    elif opcao == 0:
        exit()
            

    else:
        print("\nInsira uma opção válida.")

menu()

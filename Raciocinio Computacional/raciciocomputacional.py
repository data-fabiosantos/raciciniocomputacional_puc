# Materia: Racicinio Computacional
# Aluno:   Fábio Henrique dos Santos
# Curso:   Big Data e Inteligência Analitica

# Importação da biblioteca
import random


# Mensagem que aparecerá no início
# Repetição com while true
print('Bem vindo ao jogo Zumbi Dice! Vamos jogar?')
while True:
    try:
        jogadores = int(input("Selecione a quantidade de jogadores, podendo ser de no mínimo 2:"))
# Condição se jogador for menor que 2 mostre na tela "Quantidade inválida de jogadores"
        if jogadores < 2:
            print("Quantidade inválida de jogadores")
            continue
# Se não mostre na tela "Vamos começar o jogo"
        else:
            print("Vamos começar o jogo")
            break
    except ValueError:
        print("Valor inválido")


# Variavel "name" receberá o nome do jogador e adicionar na lista através do append
# loop de repetição for
listaPlayers = []
for i in range(jogadores):
    name = input("Informe o nome do jogador " + str(i + 1) + ":")
    listaPlayers.append(name)


verde = "CPCTPC"
amarelo = "TPCTPC"
vermelho = "TPTCPT"

listaDados = [verde, verde, verde, verde, verde, verde,
              amarelo, amarelo, amarelo, amarelo,
              vermelho, vermelho, vermelho]

print('Vamos começar...')
# Iniciando jogo, com zero participantes
playerAtual = 0

# Para jogar na lista de jogadores
# se inicia com total 0 
for jogador in listaPlayers:
    tiro = 0
    cerebro = 0
    passos = 0

    while True:
        listadadossort = []
        print('Turno do jogador', jogador)
        print('Dados sorteados:')
        for i in range(3):
# sorteia de acordo com lista de dados, de 0 a 12, total : 13
# criação de loops
            numSort = random.randint(0, 12)
            dadosorteado = listaDados[numSort]
            if dadosorteado == 'CPCTPC':
                print('Verde')
            elif dadosorteado == "TPCTPC":
                print('Amarelo')
            else:
                print('Vermelho')
            listadadossort.append(dadosorteado)
# resultados de sorteio atraves de varedura dos dados sorteados na lista
        print('As faces sorteadas foram: ')
        for dadosorteado in listadadossort:
            numero_dado = random.randint(0, 5)
            if dadosorteado[numero_dado] == "C":
                print('Você comeu um cérebro!')
                cerebro += 1
            elif dadosorteado[numero_dado] == "T":
                print('Você levou um tiro!')
                tiro += 1
            else:
                print('A vítima escapou!')
                passos += 1
# mostrar para o jogar sempre o total
        print('Você já tem:\nTiro:', tiro, '\nCérebro:', cerebro, '\nPasso:', passos)

        resp = ''
# se digitar s irá lançar novaente, n para parar.
        while True:
            escolha = input('Deseja lançar os dados novamente? (s/n)')
            if escolha == "s":
                break
            elif escolha == "n":
                resp = escolha
                break
            else:
                print('Digite "s" para sim e "n" para não.')
                continue
        if resp == "n":
            playerAtual += 1
            break
# fim de jogo
print('O jogo terminou!')

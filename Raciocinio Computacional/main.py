# Materia: Racicinio Computacional
# Aluno:   Fábio Henrique dos Santos
# Curso:   Big Data e Inteligência Analitica

# solicita players e dados: arquivos e chama algumas funções
from players import inserir,adicionar_cerebro,remover_cerebros,scoreAtual
from dados import randomDice,randomResult,resultRound

# Criação de listas vazios
facesroud = []
faces = []
dados_retirados = []
repetirDado = []
# Quantidade : 13 possibilidades
Dice = ['Verde','Verde','Verde','Verde','Verde','Verde','Vermelho','Vermelho','Vermelho','Amarelo','Amarelo','Amarelo','Amarelo']
manterJogo = True

# função 
def menu():
    print("\n",30 * '-',"Bem vindo ao Zumbi Dice",30 * '-',"\n")
    print("O objetivo do jogo é conseguir 13 Cérebros primeiro, o participante que conseguir primeiro, ganha o jogo\n"
          "Mas, preste muita atenção nos tiros em cada rodada, caso receba 3 tiros você perde todos os seus pontos\n"
          "Regras:\n"
          "01 - Permitido no máximo 05 jogadores\n"
          "02 - Quem conseguir 13 pontos primeiro, é o vencedor(a)\n"
          "03 - Levando 03 tiros em uma rodada os pontos são zerados\n"
          "04 - São 13 dados por turno, acabando os dados da caixa a rodada acaba e passa ao próximo\n"
          "05 - Caso o Dado caia com  a face 'Fugitivo' o mesmo dado poderá ser lançado novamente\n"
          "06 - Usar Letras maisculas para responder\n")

def novoRound():
    print(30 * '-',"Proximo turno", 30 * '-')
    
Jogadores = {}
menu()
# Loop define a  quantidade de jogadores, como número inteiro
# Caso quantidade jogadores seja menor que 0 imprima X informação
# Caso quantidade de jogadores for maior que 5 imprima Y informação
# Caso seja diferente imprima : digite um número valido
while True:
    try:
        Quantidade_jogadores = int(input("Digite quantos jogadores participaram: "))
        if Quantidade_jogadores < 0:
            print("Esse número de jogadores não é valido")
        elif Quantidade_jogadores > 5:
            print("Máximo de jogadores atingido, o limite é 05!")
        else: 
            break
    except ValueError:
        print("Por gentileza, digite um número valido.")

# Leia 1 jogador dentro da quantidade de jogadores selecionados +        
for i in range(1,Quantidade_jogadores+1):
    j = i
    inserir(Jogadores,i)

while manterJogo:

    for nome_jogador in Jogadores:
        scoreJogador = scoreAtual(nome_jogador,Jogadores)
        print("Sua vez {}!\n""Sua pontuação atual é de {} cérebros".format(nome_jogador,scoreJogador))
    
        while True:
            try:
                resultDados = randomDice(Dice,dados_retirados,repetirDado)
                repetirDado = resultDados[1]
                if input("Gostaria de mexer os dados? Digite S/N--") == "N":
                    novoRound()
                    break
                #Pega as faces sorteadas
                dice_faces = randomResult(resultDados[0],faces,Dice,Jogadores,nome_jogador,dados_retirados,repetirDado)
                #Valida se o jogador fez 13 pontos
                if dice_faces == 'WINNER':
                    print("Isso ai {} - você venceu a partida".format(nome_jogador))
                    sleep(100)
                    exit()
                if dice_faces == 'LOSER':
                    novoRound()
                    faces = []
                    dados_retirados = []
                    repetirDado = []
                    c = 0
                    f = 0
                    t = 0
                    Dice = ['Verde','Verde','Verde','Verde','Verde','Verde','Vermelho','Vermelho','Vermelho','Amarelo','Amarelo','Amarelo','Amarelo']
                    break
                #Valida se o jogadore tomou 3 tiros, se sim passa a rodada e perde os pontos
                if input("-----Deseja Jogar novamente?  S/N ----- ") == 'N':
                    adicionar_cerebro(nome_jogador,Jogadores,dice_faces)
                    resultRound(dice_faces,nome_jogador,Jogadores)
                    novoRound()
                    faces = []
                    dados_retirados = []
                    repetirDado = []
                    c = 0
                    f = 0
                    t = 0
                    Dice = ['Verde','Verde','Verde','Verde','Verde','Verde','Vermelho','Vermelho','Vermelho','Amarelo','Amarelo','Amarelo','Amarelo']
                    break
                dados_retirados = []
                dados_retirados.extend(repetirDado)
                
            except ValueError:
                print("Digite novamente, por favor")

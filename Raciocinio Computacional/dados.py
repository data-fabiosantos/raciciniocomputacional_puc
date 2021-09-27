# Materia: Racicinio Computacional
# Aluno:   Fábio Henrique dos Santos
# Curso:   Big Data e Inteligência Analitica

# Importação da biblioteca
import random
# Importaçao de def (funções) do arquivo.py 
from players import adicionar_cerebro,remover_cerebros



def randomDice(Dice,dados_retirados,repetirDado):
    
    print("Os dados retirados são: ")

    for v in range(3):
        if Dice != []:
            if len(dados_retirados) <= 2:
                diceResult = random.choice(Dice)
            else: 
                print("Dado(s) Reaprovetitado(s):")
                for dado in repetirDado:
                    print(dado)
                repetirDado = []
                return dados_retirados,repetirDado
                
            if diceResult == "Verde":
                Dice.remove('Verde')
                dados_retirados.append(diceResult)
                print("Verde")
            elif diceResult == "Vermelho":
                Dice.remove('Vermelho')
                dados_retirados.append(diceResult)
                print("Vermelho")
            elif diceResult == "Amarelo":
                Dice.remove('Amarelo')
                dados_retirados.append(diceResult)
                print("Amarelo")
        else:
            print("Os dados acabaram")
            break
        
    repetirDado = []
    return dados_retirados,repetirDado


# gera os resultados dos dados com base na cor dos dados
def randomResult(resultDados,faces,Dice,Jogadores,nome_jogador,dados_retirados,repetirDado):
    # receber os dados do dados e atraves disso ver como jogar os dados
    faces = []
    c = Jogadores[nome_jogador]
    f = 0
    t = 0
    Gdice = ['Cerebro','Cerebro','Cerebro','Tiro','Fugitivo','Fugitivo']
    Ydice = ['Cerebro','Cerebro','Tiro','Tiro','Fugitivo','Fugitivo']
    Rdice = ['Cerebro','Tiro','Tiro','Tiro','Fugitivo','Fugitivo']
    for i in resultDados:
        if i == 'Verde':
            g = random.choice(Gdice)
            faces.append(g)
            if g == 'Fugitivo':
                repetirDado.append('Verde')
            print(g)
        elif i == 'Amarelo':
            y = random.choice(Ydice)
            faces.append(y)
            if y == 'Fugitivo':
                repetirDado.append('Amarelo')
            print(y)
        elif i == 'Vermelho':
            r = random.choice(Rdice)
            faces.append(r)
            if r == 'Fugitivo':
                repetirDado.append('Vermelho')
            print(r)

# validar se o jogador levou 3 tiros ou teve 13 pontos
    for i in faces:
        if i == 'Cerebro':
            c = c + 1
            # valida se o jogador fez a quantidade de pontos suficiente
            if c >= 13:
                c = 'WINNER'
                return c
        elif i ==  'Passos':
            f = f + 1
            
        elif i == 'Tiro':
            t = t + 1
            # valida se o jogador levou 3 tiros, se sim mando o comando para passar ao proximo jogador
            if t >= 3:
                remover_cerebros(nome_jogador,Jogadores)
                print("Você foi baleado 3 vezes e perdeu todos os pontos")
                t = 'LOSER'
                return t
           
    return faces
    
# define o resultado de cada partida
def resultRound(dice_faces,nome_jogador,Jogadores):
    c = 0
    f = 0
    t = 0
    geral = Jogadores[nome_jogador]
    for i in dice_faces:
        if i == 'Cerebro':
            c = c + 1 
        elif i ==  'Fugitivo':
            f = f + 1 
        elif i == 'Tiro':
            t = t + 1
    print("O seu resultado nessa partida foi de: \n",c," Cerebros\n",f," Fugitivos\n",t," Tiros\n""Pontuação Geral :", geral, "Cérebro(s)")
    
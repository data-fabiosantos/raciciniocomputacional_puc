# Materia: Racicinio Computacional
# Aluno:   Fábio Henrique dos Santos
# Curso:   Big Data e Inteligência Analitica

# função que registra nome do participante e inicia contagem de cerebros 0
def dados_jogador(i):
    nome_participante = input("Por favor, escreva o nome do(a) {}º participante: ".format(i))
    cerebros = 0
    return nome_participante,cerebros


# Função inserindo quantidade de dados     
def inserir(Jogadores,i):
    jogador = dados_jogador(i)
    Jogadores[jogador[0]] = jogador[1]
    return True


# Função adicionando cerebros ao jogador
def adicionar_cerebro(nome_jogador,Jogadores,dice_faces):
    p = Jogadores[nome_jogador]
    if p > 0:        
        c = p
    else:
        c = 0
    
    for i in dice_faces:
        if i == 'Cerebro':
            c = c + 1

    Jogadores[nome_jogador] = c

    return True


# Função remover cerebros
def remover_cerebros(nome_jogador,Jogadores):
    c = 0
    Jogadores[nome_jogador] = c
    return True


# Função score
def scoreAtual(nome_jogador,Jogadores):
    
    score = Jogadores[nome_jogador]
    return score
    
import random

# Dicionário com níveis de dificuldade
niveis = {
    'Ferro': {'range_max': 10, 'tentativas': 5, 'pontos_base': 10},
    'Prata': {'range_max': 20, 'tentativas': 4, 'pontos_base': 20},
    'Platina': {'range_max': 50, 'tentativas': 3, 'pontos_base': 30},
    'Diamante': {'range_max': 100, 'tentativas': 2, 'pontos_base': 40},
    'Grão-Mestre': {'range_max': 1000, 'tentativas': 1, 'pontos_base': 50}
}

# Leaderboard: lista de tuplas (nome, pontos)
leaderboard = []

def jogar():
    print("E aí, aventureiro! Bem-vindo ao Jogo de Adivinhação Épico!")
    print("Escolha seu nível: Ferro, Prata, Platina, Diamante ou Grão-Mestre.")
    nivel = input("Digite o nível: ").strip().title()
    
    if nivel not in niveis:
        print("Nível inválido, mané! Tenta de novo.")
        return jogar()
    
    config = niveis[nivel]
    numero_secreto = random.randint(1, config['range_max'])
    tentativas_restantes = config['tentativas']
    print(f"\nBeleza! No {nivel}, adivinha um número de 1 a {config['range_max']} com {tentativas_restantes} tentativas.")
    print("Cada tentativa errada dá uma dica, e pontos no final se você ganhar!")
    
    while tentativas_restantes > 0:
        try:
            chute = int(input("Seu chute: "))
        except ValueError:
            print("Ei, só números, tá? Tenta de novo.")
            continue
        
        if chute < 1 or chute > config['range_max']:
            print(f"Chute fora do range, bro! Tem que ser entre 1 e {config['range_max']}.")
            continue
        
        if chute == numero_secreto:
            pontos = config['pontos_base'] * tentativas_restantes
            print(f"\nAêêê! Acertou, monstro! Ganhou {pontos} pontos.")
            nome = input("Digite seu nome pro leaderboard: ").strip()
            leaderboard.append((nome, pontos))
            leaderboard.sort(key=lambda x: x[1], reverse=True)
            leaderboard[:] = leaderboard[:5]  # Mantém só top 5
            break
        elif chute < numero_secreto:
            print("Muito baixo! Tenta mais alto.")
        else:
            print("Muito alto! Tenta mais baixo.")
        
        tentativas_restantes -= 1
        print(f"Tentativas restantes: {tentativas_restantes}")
    
    if tentativas_restantes == 0:
        print(f"\nPerdeu, otário! O número era {numero_secreto}. Zero pontos pra você.")
    
    mostrar_leaderboard()
    jogar_novamente = input("\nQuer jogar de novo? (s/n): ").lower()
    if jogar_novamente == 's':
        jogar()

def mostrar_leaderboard():
    if leaderboard:
        print("\n--- Leaderboard Top 5 ---")
        for i, (nome, pontos) in enumerate(leaderboard, 1):
            print(f"{i}. {nome} - {pontos} pontos")
    else:
        print("\nLeaderboard vazio ainda. Seja o primeiro!")

# Inicia o jogo
jogar()
# sorteio.py — versão simples
import random

def ler_inteiro(msg, minimo=2):
    while True:
        try:
            n = int(input(msg))
            if n >= minimo: return n
        except: pass
        print(f"Digite um número inteiro ≥ {minimo}.")

def ler_jogadores():
    print("\nDigite os nomes dos jogadores (uma linha por nome).")
    print("Pressione ENTER em branco para terminar.\n")
    jogs = []
    while True:
        nome = input("Jogador: ").strip()
        if not nome: break
        jogs.append(nome)
    return jogs

def sortear_times(jogadores, n_times, seed=None):
    if seed: random.seed(seed)
    random.shuffle(jogadores)
    times = [[] for _ in range(n_times)]
    i = 0
    for nome in jogadores:
        times[i].append(nome)
        i = (i + 1) % n_times  # distribui em rodada
    return times

def main():
    print("=== Sorteio de Times (versão simples) ===")
    n_times = ler_inteiro("Quantos times? ")
    jogadores = ler_jogadores()
    if len(jogadores) < n_times:
        print("\nTem menos jogadores do que times. Adicione mais jogadores ou reduza o nº de times.")
        return
    seed = input("\nSeed (opcional, deixe vazio para aleatório): ").strip() or None
    times = sortear_times(jogadores, n_times, seed)
    print("\n===== RESULTADO =====")
    for i, t in enumerate(times, 1):
        print(f"\nTime {i} ({len(t)} jogadores)")
        print("-"*30)
        for nome in t:
            print(nome)

if _name_ == "_main_":
    main()

from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

navios_info = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4),
]

for nome, tamanho, quantidade in navios_info:
    i = 0
    while i < quantidade:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))

        if tamanho == 1:
            orientacao = 'vertical'
        else:
            orientacao_num = int(input("[1] Vertical [2] Horizontal >"))
            if orientacao_num == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            i += 1
        else:
            print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios_oponente = 0
for lista in frota_oponente.values():
    total_navios_oponente += len(lista)

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_str = input("Jogador, qual linha deseja atacar? ")
    while not linha_str.isdigit() or not (0 <= int(linha_str) <= 9):
        print("Linha inválida!")
        linha_str = input("Jogador, qual linha deseja atacar? ")
    linha_atq = int(linha_str)

    coluna_str = input("Jogador, qual coluna deseja atacar? ")
    while not coluna_str.isdigit() or not (0 <= int(coluna_str) <= 9):
        print("Coluna inválida!")
        coluna_str = input("Jogador, qual coluna deseja atacar? ")
    coluna_atq = int(coluna_str)

    atual = tabuleiro_oponente[linha_atq][coluna_atq]
    if atual == 'X' or atual == '-':
        print(f"A posição linha {linha_atq} e coluna {coluna_atq} já foi informada anteriormente!")
        continue

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_atq, coluna_atq)

    afundados_op = afundados(frota_oponente, tabuleiro_oponente)
    if afundados_op == total_navios_oponente:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

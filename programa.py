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

print(frota)

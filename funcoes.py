def define_posicoes(linha, coluna, orientacao, tamanho):
    l = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            l.append([linha + i, coluna])
    else:
        for i in range(tamanho):
            l.append([linha, coluna + i])
    return l


def preenche_frota(dic_frota, navio, linha, coluna, orientacao, tamanho):
    dic = dic_frota
    pos = define_posicoes(linha, coluna, orientacao, tamanho)
    if navio in dic:
        dic[navio].append(pos)
    else:
        dic[navio] = [pos]
    return dic

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

    for posicoes in frota.values():
        for navios in posicoes:
            for cordenada in navios:
                tabuleiro[cordenada[0]][cordenada[1]] = 1
    return tabuleiro


def afundados(dic, tabuleiro):
    afundados = 0
    for tipo in dic.values():
        for navio in tipo:
            soma = 0
            qtd = 0
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] == 'X':
                    soma += 1
                qtd += 1
            if soma == qtd:
                afundados += 1
                
    return afundados

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        if posicao[0] > 9 or posicao[1] > 9:
            return False
        for posicoes in frota.values():
            for navio in posicoes:
                if posicao in navio:
                    return False
    return True

linha = input("Qual linha está?")
coluna = input("Qual coluna está?")
orientação = int(input("Qual direção está? (Digite 1 para vertocal e 2 para horizontal)"))
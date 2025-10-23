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
    soma = 0
    for navios in dic.values:
        for posicoes in tabuleiro:
            if posicoes == "X" and "X" not in tabuleiro[posicoes]:
                soma +=1
    return soma

def define_posicoes(linha, coluna, orientacao, tamanho):
    l = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            l.append([linha + i, coluna])
    else:
        for i in range(tamanho):
            l.append([linha, coluna + i])
    return l
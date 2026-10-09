def selection_sort(filmes, chave=lambda f: f.codigo):
    v = list(filmes)
    n = len(v)
    comparacoes = 0
    movimentacoes = 0

    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if chave(v[j]) < chave(v[indice_menor]):
                indice_menor = j
        if indice_menor != i:
            v[i], v[indice_menor] = v[indice_menor], v[i]
            movimentacoes += 2

    return v, comparacoes, movimentacoes


def insertion_sort(filmes, chave=lambda f: f.codigo):
    v = list(filmes)
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(v)):
        atual = v[i]
        chave_atual = chave(atual)
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if chave(v[j]) <= chave_atual:
                break
            v[j + 1] = v[j]          
            movimentacoes += 1
            j -= 1
        if j + 1 != i:
            v[j + 1] = atual
            movimentacoes += 1

    return v, comparacoes, movimentacoes


def bubble_sort(filmes, chave=lambda f: f.codigo):
    v = list(filmes)
    comparacoes = 0
    movimentacoes = 0
    fim = len(v) - 1

    troca = True
    while troca:
        troca = False
        for i in range(fim):
            comparacoes += 1
            if chave(v[i]) > chave(v[i + 1]):
                v[i], v[i + 1] = v[i + 1], v[i]
                movimentacoes += 2
                troca = True
        fim -= 1

    return v, comparacoes, movimentacoes

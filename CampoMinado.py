import numpy as np  # Importa a biblioteca numpy para manipulação de arrays


def carrefar_mapa(filename):
    """Carrega o mapa a partir de um arquivo de texto."""
    with open(filename, 'r') as file:  # abre o arquivo em mode de leitura
        linhas = file.readlines()  # le todos as linhnas do arquivo
        # obtem altura e lagura do mapa
        altura, largura = map(int, linhas[0].strip().split())
        # inicializ o mapa com zerros
        mapa_bombas = np.zeros((altura, largura), dtype=int)

        # Preenche o mapa com as posicoes das bombas
        for i in range(1, altura+1):
            mapa_bombas[i-1] = list(map(int, linhas[i].strip().split()))

    return mapa_bombas  # retorna o mapa das bombas


def mostrar_mapa(bombas_adjacentes, revelado):  # bombas_adjacentes=BOMBAS NAS VIZINHACAS
    """Exibe o estado atual do mapa para o jogador."""
    altura, largura = bombas_adjacentes.shape  # obtem as dimesoes do mapa
    print("Cordenadas disponiveis:")
    print("Linhas: 0 a", altura-1)  # informa as linhas dispovivel
    print("colunas: 0 a", largura-1)  # informa as colunas dispovivel

    # percorre cada elemento para exibir o mapa
    for i in range(altura):
        linha = ""  # inicializa a string da linha
        for j in range(largura):
            if revelado[i][j]:  # se o elemento foi recelado
                if bombas_adjacentes[i][j] > 0:
                    # adiciona numero de bombas na vizinhanca
                    linha += f'{bombas_adjacentes[i][j]}'
                else:
                    linha += '-'  # adicina o campo vazio
            else:
                linha += '#'  # adicina um simplo para campo nao revelado
        print(linha)  # imprime a linha do map


def jogo(mapa_bombas):
    """Controla a lógica principal do jogo Campo Minado."""
    bombas_adjacentes = calcular_bombas(
        mapa_bombas)  # calula as bombas vizinhas
    altura, largura = mapa_bombas.shape  # obtem as dimencoes do mapa
    # inicializa a matrisz de revelacao
    revelado = np.zeros((altura, largura), dtype=bool)

    while True:
        mostrar_mapa(bombas_adjacentes, revelado)  # exibe o mapa atual

        # solicita as posicao
        while True:
            try:
                linha = int(input("digite a linha:"))  # entrada da linha
                coluna = int(input("digite a colula:"))  # entrada da col

                # verifica se as posicao e valida
                if linha < 0 or linha >= altura or coluna < 0 or coluna >= largura:
                    print("coordenadas invalidas!por favor, tentar novamnte")
                else:
                    break  # Sai do lool se a possicao e valida
            except ValueError:
                print("entrada invalida!por favoe, insera numero interios")

        if mapa_bombas[linha, coluna] == 1:  # se for uma bomba
            print("voce acertou uma bomba! fim de jogoa")
            mostrar_resultado(False)  # mostra resuldado de derroda
            return False  # retorna false indicando que o jogo termino
        else:
            revelado[linha, coluna] = True  # revelaa a posicao
            # se nao tive bombas nas vizinhaca
            if bombas_adjacentes[linha, coluna] == 0:
                # revela as posicoes vizinhas
                for di in [-1, 0, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 < linha+di < altura and 0 <= coluna + dj < largura:
                            revelado[linha + di, coluna + dj] = True

        # verifica se o jogado venceu
        if np.all(revelado | mapa_bombas):
            print("Parabéns! Você venceu!")
            mostrar_resultado(True)  # Mostra o resultado de vitória
            return True  # Retorna True indicando que o jogo terminou


def calcular_bombas(mapa_bombas):
    """Calcula o número de bombas adjacentes para cada célula."""


def mostrar_resultado(vitoria):
    """Mostra o resultado final do jogo."""

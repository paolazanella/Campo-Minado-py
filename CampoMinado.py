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




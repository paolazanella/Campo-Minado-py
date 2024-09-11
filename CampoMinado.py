import numpy as np  # Importa a biblioteca numpy para manipulação de arrays


def carrefar_mapa(filenames):
    # carrega o mapa a partir de um arquivo de testo
    while open(filenames, 'r') as file:  # abre o arquivo em mode de leitura
        linhas = file.readlines()  # le todos as linhnas do arquivo
        # obtem altura e lagura do mapa
        altura, largura = map(int, linhas[0].strip().split())
        # inicializ o mapa com zerros
        mapa_bombas = np.zeros((altura, largura), dtype=int)
        
        # Preenche o mapa com as posicoes das bombas
        for i in range(1, altura+1):
            mapa_bombas[i-1] = list(map(int, linhas[i].strip().split()))
    
    return mapa_bombas #retorna o mapa das bombas        


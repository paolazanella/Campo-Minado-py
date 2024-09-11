# README - Campo Minado

## Descrição do Projeto

Este projeto recria o clássico jogo "Campo Minado" utilizando Python. O jogo é baseado nas regras tradicionais, onde o jogador deve revelar quadrados em uma grade, evitando minas. A implementação utiliza a biblioteca NumPy para gerenciar o mapa do jogo.

## Regras do Jogo

1. **Campo de Jogo**: Consiste em um campo retangular de quadrados.
2. **Revelação de Quadrados**:
   - Se um quadrado revelado contém uma mina, o jogo termina.
   - Se não contém mina, pode ocorrer:
     - Um número que indica a quantidade de minas adjacentes.
     - Nenhum número, onde os quadrados adjacentes são revelados automaticamente.
3. **Objetivo**: Ganhar ao revelar todos os quadrados sem minas.

## Estrutura do Jogo

- O jogo utiliza duas matrizes:
  - Uma matriz de strings para a visualização do estado do jogo.
  - Uma matriz de inteiros para as posições das minas.
  
### Representação do Mapa

- `-` : Campo revelado sem minas adjacentes.
- `1, 2, ...` : Campos com o número correspondente de minas adjacentes.
- `#` : Campo não revelado.

## Instruções de Uso

1. **Carregar Mapa**: O jogo inicia com o carregamento de mapas pré-definidos a partir de arquivos de texto.
2. **Entrada do Jogador**: O jogador deve inserir as coordenadas (linha e coluna) do campo a ser revelado.
3. **Resultados**:
   - Se o quadrado contém uma mina, o jogo termina.
   - Se contém minas adjacentes, o número correspondente é exibido.
   - Se não contém, o quadrado e os adjacentes são revelados.

## Arquivos de Mapa

Os mapas do jogo estão disponíveis nos seguintes arquivos de texto:
- `mapa_facil.txt`
- `mapa_medio.txt`
- `mapa_dificil.txt`

## Requisitos

- Python 3.x
- Biblioteca NumPy

## Execução

Para iniciar o jogo, execute o arquivo `campominado.py` no console.

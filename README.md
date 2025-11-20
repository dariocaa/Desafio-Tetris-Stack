# 🏗️ Desafio-Tetris-Stack: Verificação de Pontuação e Limpeza de Linhas

Este projeto em Python simula uma parte crucial da lógica de pontuação do jogo Tetris: a **verificação, limpeza e queda** de blocos após uma ou mais linhas serem completadas.

O objetivo deste código é praticar o manuseio de **matrizes 2D (listas de listas)** e a implementação de algoritmos de manipulação de dados que simulam o movimento de queda.

## 🎯 Objetivo do Desafio

O desafio reside na função `verificar_e_limpar_linhas(grid)`:

1.  **Identificar Linhas Completas:** Varrer o grid (tabuleiro) e encontrar todas as linhas onde todas as 10 células estão preenchidas (representadas pelo valor `1`).
2.  **Calcular a Pontuação:** Usar o dicionário `PONTUACAO_POR_LINHAS` para calcular a pontuação correta com base no número de linhas limpas simultaneamente (o famoso bônus por "Tetris" - 4 linhas).
3.  **Simular a Queda (Stack):** Criar um novo grid removendo as linhas completas e adicionando linhas vazias (`0`) no topo para simular a "queda" (descida) dos blocos restantes.

## 🚀 Como Executar

### 1. Pré-requisitos

Certifique-se de que o **Python 3** está instalado em sua máquina.

### 2. Baixar e Salvar o Código

Copie o código Python do desafio e salve-o em um arquivo chamado `desafio_tetris_stack.py`.

### 3. Execução

Abra seu terminal ou prompt de comando, navegue até o diretório do arquivo e execute o comando:

```bash
python desafio_tetris_stack.py

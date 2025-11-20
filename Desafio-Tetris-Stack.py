import pprint

# Configurações do Jogo
LARGURA = 10
ALTURA = 20

# Dicionário de Pontuação
PONTUACAO_POR_LINHAS = {
    1: 100,
    2: 300,
    3: 500,
    4: 800  # Tetris!
}

def criar_grid_vazio():
    """Cria um grid 20x10 preenchido com 0 (vazio)."""
    return [[0] * LARGURA for _ in range(ALTURA)]

def simular_empilhamento(grid):
    """
    Função que simula o estado do grid após algumas jogadas.
    1 representa um bloco preenchido, 0 representa espaço vazio.
    """
    # Linhas de Exemplo (Índices 15 a 19 - contando de baixo para cima)
    
    # Linha 19 (Topo - Vazia)
    grid[19] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    
    # Linha 18 (Quase Completa)
    grid[18] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0] 
    
    # Linha 17 (Completa)
    grid[17] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
    
    # Linha 16 (Completa)
    grid[16] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
    
    # Linha 15 (Completa)
    grid[15] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 

    # Linhas abaixo (Ex: 0 a 14) permanecem vazias
    return grid

def verificar_e_limpar_linhas(grid):
    """
    Varre o grid de baixo para cima, identifica linhas completas, 
    calcula a pontuação e remove as linhas, "descendo" o resto do grid.
    Retorna a pontuação total e o novo grid.
    """
    linhas_a_limpar = []
    
    # 1. Identificar Linhas Completas
    for i in range(ALTURA):
        # Uma linha é completa se a soma de seus elementos for igual à LARGURA (todos são '1')
        if sum(grid[i]) == LARGURA:
            linhas_a_limpar.append(i)
            
    num_linhas_limpas = len(linhas_a_limpar)
    
    if num_linhas_limpas == 0:
        return 0, grid # Nenhuma pontuação, grid inalterado

    # 2. Calcular Pontuação
    pontuacao = PONTUACAO_POR_LINHAS.get(num_linhas_limpas, 0)
    
    print(f"\n🎉 **Linhas Limpas:** {num_linhas_limpas}")
    print(f"Linhas removidas nos índices: {linhas_a_limpar}")
    print(f"Pontuação base: {pontuacao}")

    # 3. Limpar Linhas e Descer o Grid
    
    # Cria um novo grid apenas com as linhas que NÃO foram limpas
    novo_grid = [grid[i] for i in range(ALTURA) if i not in linhas_a_limpar]
    
    # Adiciona as novas linhas vazias (0) no topo
    linhas_vazias_novas = [[0] * LARGURA for _ in range(num_linhas_limpas)]
    
    # Concatena as novas linhas vazias com o resto do grid
    grid_final = linhas_vazias_novas + novo_grid
    
    return pontuacao, grid_final

# --- Execução do Desafio ---

grid_inicial = criar_grid_vazio()
grid_com_pilha = simular_empilhamento(grid_inicial)

print("## Estado Inicial do Grid (Antes da Pontuação)")
pprint.pprint(grid_com_pilha)


pontuacao_total, grid_apos_limpeza = verificar_e_limpar_linhas(grid_com_pilha)

print("\n--- Resultado ---")
print(f"**Pontuação Total Ganha:** {pontuacao_total} pontos")

print("\n## Estado Final do Grid (Após a Limpeza)")
pprint.pprint(grid_apos_limpeza)
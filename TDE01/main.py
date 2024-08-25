# Fernando Alonso Piroga da Silva

# ENUNCIADO
# O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
# seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
# operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas.
# A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
# dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
# a informação e a formatação mostrada a seguir:
# União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
# Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
# um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
# de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
# minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima. 

# ALTERAR NÚMERO DO TESTE PARA TESTES DIFERENTES
with open("testes/teste3.txt", "r") as file:
    arquivo = file.readlines()

numOperacoes = int(arquivo[0])
linhaAtual = 1

for i in range(numOperacoes):
    operacao = arquivo[linhaAtual].strip()
    conjunto1 = set(arquivo[linhaAtual + 1].strip().split(', '))
    conjunto2 = set(arquivo[linhaAtual + 2].strip().split(', '))
    
    # transformei em uma lista na hora de imprimir na tela para poder remover as '' dos elementos
    # e ficar formatado da mesma forma que estava no enunciado.
    if operacao == 'U':
        resultado = conjunto1 | conjunto2
        conjunto1_str = ', '.join(conjunto1)
        conjunto2_str = ', '.join(conjunto2)
        resultado_str = ', '.join(resultado)
        print(f"União: conjunto 1 {{{conjunto1_str}}}, conjunto 2 {{{conjunto2_str}}}. Resultado: {{{resultado_str}}}")
    elif operacao == 'I':
        resultado = conjunto1 & conjunto2
        conjunto1_str = ', '.join(conjunto1)
        conjunto2_str = ', '.join(conjunto2)
        resultado_str = ', '.join(resultado)
        print(f"Intersecção: conjunto 1 {{{conjunto1_str}}}, conjunto 2 {{{conjunto2_str}}}. Resultado: {{{resultado_str}}}")
    elif operacao == 'D':
        resultado = conjunto1 - conjunto2
        conjunto1_str = ', '.join(conjunto1)
        conjunto2_str = ', '.join(conjunto2)
        resultado_str = ', '.join(resultado)
        print(f"Diferença: conjunto 1 {{{conjunto1_str}}}, conjunto 2 {{{conjunto2_str}}}. Resultado: {{{resultado_str}}}")
    elif operacao == 'C':
        resultado = []
        for elementoX in conjunto1:
            for elementoY in conjunto2:
                resultado.append(f'({elementoX}, {elementoY})')
        conjunto1_str = ', '.join(conjunto1)
        conjunto2_str = ', '.join(conjunto2)
        resultado_str = ', '.join(resultado)
        print(f"Produto Cartesiano: conjunto 1 {{{conjunto1_str}}}, conjunto 2 {{{conjunto2_str}}}. Resultado: {{{resultado_str}}}")
    
    linhaAtual += 3
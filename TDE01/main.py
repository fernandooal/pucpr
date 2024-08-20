# Fernando Alonso Piroga da Silva
with open("testes/teste1.txt", "r") as file:
    arquivo = file.readlines()

numOperacoes = int(arquivo[0])
linhaAtual = 1

for i in range(numOperacoes):
    operacao = arquivo[linhaAtual].strip()
    conjunto1 = set(arquivo[linhaAtual + 1].strip().split(', '))
    conjunto2 = set(arquivo[linhaAtual + 2].strip().split(', '))
    
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
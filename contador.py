import sys
from collections import defaultdict


def contar_palavras(caminho_arquivo):
    # Dicionário onde a chave é a palavra e o valor é a contagem
    # defaultdict(int) inicia contagem com 0 automaticamente se a chave não existir
    frequencia = defaultdict(int)

    try:
        # Context Manager ('with') garante que o arquivo será fechado
        # mesmo se der erro, liberando o descritor de arquivo do SO.
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # remove espaços em branco (strip) e divide por espaço (split)
                palavras = linha.strip().split()
                for palavra in palavras:
                    # Normaliza para minúsculo para 'Python' == 'python'
                    frequencia[palavra.lower()] += 1

        return frequencia

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        sys.exit(1)  # Código de saída 1 indica erro no Linux


if __name__ == "__main__":
    # Verifica se o usuário passou o nome do arquivo como argumento
    if len(sys.argv) < 2:
        print("Uso correto: python contador.py <nome_do_arquivo>")
        sys.exit(1)

    arquivo_alvo = sys.argv[1]
    resultado = contar_palavras(arquivo_alvo)

    print(f"--- Frequência de palavras em {arquivo_alvo} ---")
    # Ordena o resultado por contagem decrescente (mais frequente primeiro)
    # Explicarei lambda numa próxima, mas entenda como uma função anônima de ordenação
    for palavra, qtd in sorted(resultado.items(), key=lambda item: item[1], reverse=True):
        print(f"{palavra}: {qtd}")
# kwargs significa “keyword arguments”. Aqui usamos o asterisco duplo `**` para identificar argumentos de
# palavras-chave. Ele permite que uma função aceite um número arbitrário de argumentos de palavras-chave, que formam
# um dicionário dentro da função. Essa estrutura semelhante a um dicionário permite que você acesse os valores usando
# suas respectivas chaves.

# OBS:. Você pode usar outro nome invés de kwargs, veja o exemplo:

def display_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

display_info(Nome="Stephanie", Idade=28, Profissao="Data Engineer", Mae="Luciene")
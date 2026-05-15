def cast_to_int_or_none(lista_strings):
    resultados = []
    for item in lista_strings:
        try:
            resultados.append(int(item))
        except (ValueError, TypeError):
            resultados.append(None)
    return resultados

dados = ["42", "10", "bah", "3.14", None, "-5"]
print(cast_to_int_or_none(dados)) 

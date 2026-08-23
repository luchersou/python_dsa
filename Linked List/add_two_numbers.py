def somar_dois_numeros(lista1: No, lista2: No) -> No:
    """
    Soma dois números representados como listas encadeadas,
    onde cada nó é um dígito e os números estão na ordem inversa
    (o primeiro nó é a unidade, depois a dezena, etc).

    Ideia: simular a soma "na mão", dígito por dígito,
    carregando o "vai um" (carry) pra próxima casa.
    """
    no_fictício = No(valor=None)
    atual_resultado = no_fictício
    vai_um = 0

    while lista1 is not None or lista2 is not None or vai_um != 0:
        valor1 = lista1.valor if lista1 is not None else 0
        valor2 = lista2.valor if lista2 is not None else 0

        soma = valor1 + valor2 + vai_um
        vai_um = soma // 10
        digito = soma % 10

        atual_resultado.proximo = No(valor=digito)
        atual_resultado = atual_resultado.proximo

        if lista1 is not None:
            lista1 = lista1.proximo
        if lista2 is not None:
            lista2 = lista2.proximo

    return no_fictício.proximo
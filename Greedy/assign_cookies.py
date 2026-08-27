class Solucao:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        gulas_das_criancas = sorted(g)
        tamanhos_dos_biscoitos = sorted(s)

        indice_crianca = 0
        indice_biscoito = 0
        criancas_satisfeitas = 0

        while indice_crianca < len(gulas_das_criancas) and indice_biscoito < len(tamanhos_dos_biscoitos):
            gula_da_crianca = gulas_das_criancas[indice_crianca]
            tamanho_do_biscoito = tamanhos_dos_biscoitos[indice_biscoito]

            if tamanho_do_biscoito >= gula_da_crianca:
                # O biscoito é grande o suficiente: satisfaz essa criança
                criancas_satisfeitas += 1
                indice_crianca += 1

            # Independentemente de satisfazer ou não, esse biscoito já foi avaliado
            indice_biscoito += 1

        return criancas_satisfeitas
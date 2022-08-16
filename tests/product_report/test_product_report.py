from inventory_report.inventory.product import Product


def test_relatorio_produto():
    assert (
        Product(
            0,  # id
            "farinha",  # nome_do_produto
            "Farinini",  # nome_da_empresa
            "01-05-2021",  # data_de_fabricacao
            "02-06-2023",  # data_de_validade
            "12345678",  # numero_de_serie
            "ao abrigo de luz",  # instrucoes_de_armazenamento
        ).__repr__()
        == "\
O produto farinha fabricado em 01-05-2021 por Farinini com validade \
até 02-06-2023 precisa ser armazenado ao abrigo de luz."
    )

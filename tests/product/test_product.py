from inventory_report.inventory.product import Product


def test_cria_produto():
    assert (
        Product(
            0,  # id
            "produto nome",  # nome_do_produto
            "empresa nome",  # nome_da_empresa
            "2022-02-22",  # data_de_fabricacao
            "2023-03-23",  # data_de_validade
            "12345678",  # numero_de_serie
            "Armazenar em local ventilado",  # instrucoes_de_armazenamento
        ).__repr__()
        == "\
O produto produto nome fabricado em 2022-02-22 por empresa nome com validade \
até 2023-03-23 precisa ser armazenado Armazenar em local ventilado."
    )

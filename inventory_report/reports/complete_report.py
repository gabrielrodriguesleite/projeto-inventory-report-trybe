from inventory_report.reports.simple_report import (
    SimpleReport,
    data_fab_antiga,
    data_val_proxima,
    emp_mais_produtos,
)


def produtos_por_empresa(list):
    m = {}
    for e in list:
        if e["nome_da_empresa"] in m:
            m[e["nome_da_empresa"]] += 1
        else:
            m[e["nome_da_empresa"]] = 1
    s = ""
    for e in m:
        s += f"- {e}: {m[e]}\n"

    return s


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list):
        return (
            f"Data de fabricação mais antiga: {data_fab_antiga(list)}\n"
            f"Data de validade mais próxima: {data_val_proxima(list)}\n"
            f"Empresa com mais produtos: {emp_mais_produtos(list)}\n"
            "Produtos estocados por empresa:\n"
            f"{produtos_por_empresa(list)}"
        )

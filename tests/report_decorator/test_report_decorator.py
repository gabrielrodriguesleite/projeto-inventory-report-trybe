from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    assert ColoredReport(SimpleReport).generate(
        JsonImporter.import_data("./inventory_report/data/inventory.json")
    ) == (
        "\x1b[32mData de fabricação mais antiga:\x1b[0m \x1b[36m2020-09-06"
        "\x1b[0m\n\x1b[32mData de validade mais próxima:\x1b[0m \x1b[36m20"
        "23-09-17\x1b[0m\n\x1b[32mEmpresa com mais produtos:\x1b[0m \x1b[3"
        "1mTarget Corporation\x1b[0m"
    )

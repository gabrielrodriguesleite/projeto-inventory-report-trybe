import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, arquivo):
        if arquivo.split(".")[-1] != "json":
            raise ValueError("Arquivo inválido")

        with open(arquivo, encoding="utf8") as file:
            return json.load(file)

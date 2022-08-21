import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, arquivo):
        if arquivo.split(".")[-1] != "csv":
            raise ValueError("Arquivo inválido")

        result = []
        with open(arquivo, encoding="utf8") as file:
            header, *data = csv.reader(file, delimiter=",", quotechar='"')
            for i in data:
                ob = {}
                for j in range(len(header)):
                    ob[header[j]] = i[j]
                result.append(ob)
        return result

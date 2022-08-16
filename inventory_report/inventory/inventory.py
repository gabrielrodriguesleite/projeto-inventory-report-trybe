import csv
import json

from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(arq, tipo):
        result = []
        with open(arq, encoding="utf8") as file:
            if '.csv' in arq:
                header, *data = csv.reader(file, delimiter=",", quotechar='"')
                for i in data:
                    ob = {}
                    for j in range(len(header)):
                        ob[header[j]] = i[j]
                    result.append(ob)
            elif '.json' in arq:
                result = json.load(file)

        if tipo == "simples":
            return SimpleReport.generate(result)
        else:
            return CompleteReport.generate(result)

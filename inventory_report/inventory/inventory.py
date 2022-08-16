import csv

from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(arq, tipo):
        with open(arq, encoding="utf8") as file:
            sData = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = sData
        result = []
        for i in data:
            ob = {}
            for j in range(len(header)):
                ob[header[j]] = i[j]
            result.append(ob)
        if tipo == "simples":
            return SimpleReport.generate(result)
        else:
            return CompleteReport.generate(result)

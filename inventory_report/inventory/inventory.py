import csv
import json
import xml.etree.cElementTree as et

from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


def csv_decode(file):
    result = []
    header, *data = csv.reader(file, delimiter=",", quotechar='"')
    for i in data:
        ob = {}
        for j in range(len(header)):
            ob[header[j]] = i[j]
        result.append(ob)
    return result


def xml_decode(f):
    return [{e.tag: e.text for e in r} for r in et.parse(f).getroot()]


class Inventory:
    @staticmethod
    def import_data(arq, tipo):
        result = []
        with open(arq, encoding="utf8") as file:
            if ".csv" in arq:
                result = csv_decode(file)
            elif ".json" in arq:
                result = json.load(file)
            elif ".xml" in arq:
                result = xml_decode(file)
            else:
                raise TypeError

        if tipo == "simples":
            return SimpleReport.generate(result)
        else:
            return CompleteReport.generate(result)

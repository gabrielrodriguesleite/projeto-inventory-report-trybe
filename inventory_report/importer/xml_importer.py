from inventory_report.importer.importer import Importer
import xml.etree.cElementTree as et


class XmlImporter(Importer):
    @classmethod
    def import_data(self, arquivo):
        if arquivo.split(".")[-1] != "xml":
            raise ValueError("Arquivo inválido")

        with open(arquivo, encoding="utf8") as f:
            return [{e.tag: e.text for e in r} for r in et.parse(f).getroot()]

import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) != 3:
        print("Verifique os argumentos", file=sys.stderr)
    else:
        a = sys.argv[1]
        t = sys.argv[2]
        if "csv" in a:
            print(InventoryRefactor(CsvImporter).import_data(a, t), end='')
        elif "xml" in a:
            print(InventoryRefactor(XmlImporter).import_data(a, t), end='')
        else:
            print(InventoryRefactor(JsonImporter).import_data(a, t), end='')


if __name__ == "__main__":
    main()

from datetime import date


def data_fab_antiga(lista):
    # YYYY-MM-DD
    e = lista[0]
    for i in range(len(lista)):
        d1 = date.fromisoformat(lista[i]["data_de_fabricacao"])
        d2 = date.fromisoformat(e["data_de_fabricacao"])
        if d1 < d2:
            e = lista[i]
    return e["data_de_fabricacao"]


def data_val_proxima(lista):
    # YYYY-MM-DD
    e = lista[0]
    for i in range(len(lista)):
        d1 = date.fromisoformat(lista[i]["data_de_validade"])
        d2 = date.fromisoformat(e["data_de_validade"])

        if d1 < d2 and date.today() < d1:
            e = lista[i]
    return e["data_de_validade"]


def emp_mais_produtos(lista):
    emp = {}
    for i in lista:
        if i["nome_da_empresa"] not in emp:
            emp[i["nome_da_empresa"]] = 1
        else:
            emp[i["nome_da_empresa"]] += 1
    n = -1
    e = ""
    for j in emp:
        if emp[j] > n:
            n, e = emp[j], j

    return e


class SimpleReport:
    @classmethod
    def generate(self, list):
        return (
            f"Data de fabricação mais antiga: {data_fab_antiga(list)}\n"
            f"Data de validade mais próxima: {data_val_proxima(list)}\n"
            f"Empresa com mais produtos: {emp_mais_produtos(list)}"
        )


# if __name__ == "__main__":
# print(
#     emp_mais_produtos(
#         [
#             {"nome_da_empresa": "Forces of Nature"},
#             {"nome_da_empresa": "Forces"},
#             {"nome_da_empresa": "Nature"},
#             {"nome_da_empresa": "Forces"},
#             {"nome_da_empresa": "Forces of Nature"},
#             {"nome_da_empresa": "Forces"},
#             {"nome_da_empresa": "Nature"},
#             {"nome_da_empresa": "Forces"},
#             {"nome_da_empresa": "Forces"},
#             {"nome_da_empresa": "Forces of Nature"}
#         ]
#     )
# )
# print(data_fab_antiga([
#     {"data_de_fabricacao": "2016-04-04"},
#     {"data_de_fabricacao": "2021-04-04"},
#     {"data_de_fabricacao": "2020-04-04"},
#     {"data_de_fabricacao": "2017-04-04"},
#     {"data_de_fabricacao": "2022-04-04"},
#     {"data_de_fabricacao": "2018-04-04"},
#     {"data_de_fabricacao": "2019-04-04"},
#     {"data_de_fabricacao": "2015-04-04"},
# ]))

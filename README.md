# Projeto Inventory Report - Trybe

Trybe / Desenvolvimento Web / Ciência da computação

2° Projeto desenvolvido no 4° módulo de Desenvolvimento Web da Trybe (08/22)

## Tecnologias utilizadas:

 - Python3
 - Pytest
 - Black
 - Flake8
 - Docker
 - Docker-compose
 - Linux
 - Git
 - Github

  <img src="github_avaliador.jpeg" alt=""  style="float: right" width="50%" >
  <img src="trybe_avaliador.png" alt=""  width="49%" >
  <img src="pytest_avaliador.png" alt="" width="49%" >



## Habilidades validadas:

`POO` - Programação orientada a objetos 

`SOLID` - Single responsibility, Open/closed, Dependency inversion, Liskov Substitiuition, Interface segregation.

`Padrões de projeto` - Strategy, Inhenritance, Composition etc.

`Código Limpo e de fácil manutenção` - Linter

`Leitura e escrita de arquivos` (XML, CSV, JSON)

`TDD` - Desenvolvimento dirigido a teste

## Objetivo:

Projeto gerador de relatórios, simples e completo, alimentado por arquivos com dados de estoque.

Gera como saída um relatório sobre estes dados, provenientes de arquivos dos tipos: XML, CSV e JSON.

## Para executar:

É possível executar os testes usando Docker e Docker-compose

```sh
docker-compose run --rm inventory pytest
```

É possível acessar a imagem criada acima, instalar o projeto e executar com os comandos:

```
docker run -it projeto-inventory-report-trybe_inventory bash
pip install .
python -m inventory_report.main inventory_report/data/inventory.csv completo
python -m inventory_report.main inventory_report/data/inventory.xml simples
```



### Fontes:

Todos os arquivos que não estiverem listados aqui são de autoria de [trybe-teck-ops](https://github.com/trybe-tech-ops)

Arquivos desenvolvidos por mim:

- inventory_report/main.py
- inventory_report/importer/csv_importer.py
- inventory_report/importer/importer.py
- inventory_report/importer/json_importer.py
- inventory_report/importer/xml_importer.py

- inventory_report/inventory/inventory.py
- inventory_report/inventory/inventory_iterator.py
- inventory_report/inventory/inventory_refactor.py

- inventory_report/reports/complete_report.py
- inventory_report/reports/simmple_report.py

- tests/products/test_product.py
- tests/product_report/test_product_report.py
- tests/report_decorator/test_report_decorator.py

---

####
TODO:
- Comandos de execução de cada módulo do projeto
- Comandos de execução de cada teste do projeto

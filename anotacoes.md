# Anotações — Análise Bike Sales

Arquivo de rascunho pra consolidar aprendizados e servir de base pro README.

---

## Sobre o projeto

- **Dataset:** `uncleaned_bike_sales_data.xlsx` (89 registros de vendas de bicicletas, dez/2021)
- **Objetivo:** análise exploratória — limpeza, tratamento e extração de insights de vendas
- **Notebook principal:** `analise_bike_sales.ipynb`
- **Dataset tratado:** `cleaned_bike_sales_data.csv` (separador `;`)

---

## Etapas de limpeza aplicadas

1. Remoção de espaços nos nomes das colunas (`.str.strip()`)
2. Exclusão de colunas redundantes/desnecessárias (`Year`, `Day`, `Month`, `Product_Description`, `Cost`, `Revenue`)
3. Renomeação para PT-BR (dicionário `colunas_pt`)
4. Remoção de duplicatas por `pedido_venda`
5. Recategorização de `faixa_etaria` via `pd.cut` (recria a coluna a partir de `idade_cliente`, tratando nulos)
6. Preenchimento de `quantidade` nula com `1.0`
7. Conversão de tipos (`int`, `float`)
8. Exportação para CSV

---

## Aprendizados

### Granularidade: agregar em um nível ≠ agregar em outro

Ao rodar o **top 5 de estados mais lucrativos**, percebi que **3 dos 5 estados eram australianos**. A conclusão intuitiva era: "então a Austrália é o país mais lucrativo".

Mas ao reagregar os dados **por país**, o ranking foi:

```
United States    56543.0
Australia        50326.0
France           20981.0
Germany          13636.0
Canada            9123.0
```

Os **EUA ficaram em 1º**, mesmo sem estados no topo do ranking anterior. Ou seja: a Austrália tinha poucos estados com lucro alto, mas os EUA tinham muitos estados com lucro médio — e a soma dos médios superou a dos altos.

**Lição:** o resultado de uma agregação em um nível (estado) **não permite inferir** o resultado em outro nível (país). Sempre que mudar a granularidade — estado → país, dia → mês, produto → categoria — é preciso **reagregar os dados do zero**, nunca deduzir a partir do top-N de outro nível.

---

## Insights preliminares

- **País mais lucrativo:** United States (~56.5k)
- **Estados no top 5 de lucro:** 3 são australianos (mas Austrália é 2ª no ranking de países)
- _(preencher com mais insights conforme análise avança)_

---

## Passos da análise

- [x] 5 estados mais lucrativos
- [x] 5 países mais lucrativos
- [x] Ticket médio (lucro por pedido, por país)
- [x] Grupos (idade) mais vendidos
- [x] Grupos (sexo) mais vendidos
- [x] Evolução do lucro ao longo dos dias (série temporal)

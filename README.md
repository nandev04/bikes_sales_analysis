# Análise de Vendas de Bicicletas

Projeto de análise exploratória (EDA) sobre um dataset de vendas de bicicletas referente a **dezembro de 2021**. O objetivo é praticar o fluxo completo de um projeto de análise: tratamento dos dados brutos, análise exploratória, visualizações e extração de insights.

## Dataset

- **Fonte:** [Kaggle](https://www.kaggle.com/) — arquivo `uncleaned_bike_sales_data.xlsx` (dados brutos, 89 linhas × 19 colunas)
- **Período:** 01/12/2021 a 24/12/2021
- **Escopo:** 5 países (Estados Unidos, Austrália, França, Alemanha, Canadá), dados de gênero, faixa etária, produto, quantidade, custo, preço e lucro
- **Arquivo tratado:** `cleaned_bike_sales_data.csv` (87 linhas × 13 colunas, gerado pelo `limpeza.py`)

## Estrutura do projeto

```
bike_sales/
├── uncleaned_bike_sales_data.xlsx   # dados brutos (entrada)
├── limpeza.py                       # pipeline de limpeza (ETL)
├── cleaned_bike_sales_data.csv      # dataset tratado (saída da limpeza)
├── analise_bike_sales.ipynb         # notebook de análise + insights
├── anotacoes.md                     # aprendizados durante o projeto
├── proximos_estudos.md              # tópicos a estudar em seguida
└── README.md
```

## Pré-requisitos

- Python 3.10+
- Pacotes: `pandas`, `matplotlib`, `openpyxl`, `jupyter`

Instalação recomendada (com ambiente virtual):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install pandas matplotlib openpyxl jupyter
```

## Como executar

### 1. Rodar a limpeza

Gera (ou regenera) o `cleaned_bike_sales_data.csv` a partir do `.xlsx` bruto:

```powershell
python limpeza.py
```

Só é necessário rodar novamente se o dataset bruto ou o script de limpeza mudarem.

### 2. Abrir o notebook

```powershell
jupyter notebook analise_bike_sales.ipynb
```

Ou abrir diretamente no VS Code. O notebook lê o CSV tratado, por isso a limpeza precisa ter sido executada pelo menos uma vez.

## Etapas do tratamento (`limpeza.py`)

1. Remover colunas desnecessárias (`Year`, `Day`, `Month`, `Product_Description`, `Cost`, `Revenue` — redundantes ou não usadas)
2. Padronizar nomes de colunas (traduzir para PT-BR)
3. Recodificar valores (`M`/`F` → `Masculino`/`Feminino`)
4. Remover pedidos duplicados
5. Recategorizar `faixa_etaria` com base em `idade_cliente` (bins: `<25`, `25-34`, `35-64`, `64+`)
6. Preencher `quantidade` nula com `1`
7. Converter tipos numéricos

## Análises realizadas

- Top 5 estados por lucro
- Top 5 países por lucro
- Ticket médio (receita) por país
- Ranking de pedidos por faixa etária
- Distribuição de pedidos por gênero
- Ticket médio por gênero
- Evolução do lucro ao longo dos dias

## Principais insights

1. **Estados Unidos lidera o lucro por país**, apesar de a Austrália ter mais estados no top 5 por lucro. Muitos estados com lucro médio somam mais do que poucos estados com lucro alto.
2. **Adultos (35-64) concentram ~53% dos pedidos**, seguidos de jovens adultos (~36%) e jovens (~11%). A distribuição faz sentido para o mix de produtos (bicicletas de estrada, mountain bikes, acessórios).
3. **Público feminino lidera** tanto em quantidade (57,5% vs 42,5%) quanto em ticket médio (~10% acima do masculino).
4. **Lucro diário é volátil:** em 24 dias, a meta de $10.000,00 foi batida em apenas 4 dias, com picos anômalos nos dias 18 e 19 (+47% e +214% acima da meta) seguidos de quedas bruscas.

## Aprendizados

- **Granularidade importa:** o resultado de uma agregação em um nível (estado) não permite inferir o resultado em outro nível (país). Sempre reagregar do zero ao mudar de granularidade.
- **Ticket médio ≠ lucro médio:** ticket médio é uma métrica de receita (`quantidade × preço_unitário`), não de lucro.

Mais detalhes e outros aprendizados estão em [`anotacoes.md`](anotacoes.md).

## Ferramentas

- **Python** (pandas, matplotlib)
- **Jupyter Notebook**
- **Excel** (dataset de entrada)

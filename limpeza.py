"""Pipeline de limpeza do dataset de vendas de bicicletas.

Lê `uncleaned_bike_sales_data.xlsx`, aplica os tratamentos necessários e
salva o resultado em `cleaned_bike_sales_data.csv`.

Execute com: `python limpeza.py`
"""

import pandas as pd


df = pd.read_excel('uncleaned_bike_sales_data.xlsx')

# Padronizar nomes de colunas (remover espaços e traduzir para PT)
df.columns = df.columns.str.strip()

df = df.drop(columns=['Year', 'Day', 'Month', 'Product_Description', 'Cost', 'Revenue'])

colunas_pt = {
    'Sales_Order #': 'pedido_venda',
    'Date': 'data',
    'Customer_Age': 'idade_cliente',
    'Age_Group': 'faixa_etaria',
    'Customer_Gender': 'genero_cliente',
    'Country': 'pais',
    'State': 'estado',
    'Product_Category': 'categoria_produto',
    'Sub_Category': 'subcategoria',
    'Order_Quantity': 'quantidade',
    'Unit_Cost': 'custo_unitario',
    'Unit_Price': 'preco_unitario',
    'Profit': 'lucro',
}
df = df.rename(columns=colunas_pt)

# Normalizar espaços dos valores de texto (ex: "United  States" -> "United States")
for col in df.select_dtypes(include='str').columns:
    df[col] = df[col].str.replace(r'\s+', ' ', regex=True).str.strip()

# Renomear valores de coluna
df['genero_cliente'] = df['genero_cliente'].map({'M': 'Masculino', 'F': 'Feminino'})

# Remover duplicatas
df = df.drop_duplicates(subset=['pedido_venda'])

# Tratar valores nulos
bins_idade = [0, 24, 34, 64, float('inf')]
labels_idade = ['Youth (<25)', 'Young Adults (25-34)', 'Adults (35-64)', 'Seniors (64+)']
df['faixa_etaria'] = pd.cut(
    df['idade_cliente'],
    bins=bins_idade,
    labels=labels_idade,
    right=True,
)

df['quantidade'] = df['quantidade'].fillna(1.0)

# Converter tipos
df['quantidade'] = df['quantidade'].astype(int)
df['custo_unitario'] = df['custo_unitario'].astype(float)
df['preco_unitario'] = df['preco_unitario'].astype(float)
df['lucro'] = df['lucro'].astype(float)

# Salvar dataset tratado
df.to_csv('cleaned_bike_sales_data.csv', index=False, sep=';')
print(f'Dataset tratado salvo em cleaned_bike_sales_data.csv ({len(df)} linhas).')

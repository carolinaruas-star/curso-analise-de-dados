# 📊 Mini-Projeto Avaliativo — Análise de Dados com Python

**Turma:** `Analise_de_Dados_T9`  
**Módulo:** 1 — Análise de Dados com Python  
**Projeto:** Análise Exploratória de Dados de Varejo  
**Nome Aluna:** Ana Carolina Pereira Ruas  
**Professor:** Renisson Rodrigues De Souza 

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte do **Mini-Projeto Avaliativo do Módulo 1 — Análise de Dados com Python**, com o objetivo de aplicar, de forma prática, conceitos de **importação, transformação, limpeza, análise exploratória, estatística descritiva, agrupamentos e documentação de dados**.

A proposta consiste em trabalhar com uma base de registros de varejo, realizando um processo estruturado de preparação e exploração dos dados para identificar problemas de qualidade e obter informações úteis a partir da base.

O projeto busca transformar dados inicialmente brutos em uma estrutura mais organizada e adequada para análises posteriores, mantendo o processo **reprodutível, documentado e organizado**.

---

## 🎯 Objetivos

O projeto tem como principais objetivos:

- Importar e inspecionar uma base de dados de varejo;
- Identificar problemas de qualidade nos dados;
- Trabalhar com diferentes tipos de dados;
- Realizar transformações e padronizações;
- Identificar e tratar valores ausentes;
- Identificar e remover registros duplicados;
- Converter datas para o tipo adequado;
- Realizar estatística descritiva;
- Criar agrupamentos para análise exploratória;
- Extrair informações relevantes da base;
- Documentar as decisões tomadas durante o processo;
- Preparar uma base limpa para análises futuras.

---

## 🗂️ Base de dados

A base utilizada no projeto é:

```text
Base Varejo.csv
```

Após a leitura inicial, foram identificadas **830.000 linhas** e 14 colunas no arquivo original.

Durante a inspeção, foram identificadas **4 colunas completamente vazias**, decorrentes da estrutura do arquivo CSV. Essas colunas foram removidas por não apresentarem informações úteis para a análise.

Após essa etapa, foram consideradas as seguintes colunas:

| Coluna | Descrição |
| :--- | :--- |
| `DATA` | Data da compra |
| `CO_ID` | Identificador da compra |
| `CL_ID` | Identificador do cliente |
| `CL_GENERO` | Gênero do cliente |
| `CL_EC` | Campo cadastral do cliente |
| `CL_FHL` | Número de filhos utilizado na análise estatística |
| `CL_SEG` | Segmento do cliente |
| `PR_ID` | Identificador do produto |
| `PR_CAT` | Categoria do produto |
| `PR_NOME` | Nome do produto |

> **Observação:** o material fornecido não apresenta uma definição textual para todos os códigos das colunas. Por isso, o projeto evita atribuir significados que não estejam documentados na base ou no material da atividade.

---

## 🛠️ Tecnologias utilizadas

- 🐍 Python
- 🐼 Pandas
- 📊 Matplotlib
- 📄 CSV
- 🔎 `csv.DictReader`
- 📓 Google Colab / VS Code
- 🌱 Git e GitHub

---

# 🔄 Processo de análise

O desenvolvimento foi organizado em etapas correspondentes às sprints propostas no projeto.

---

## 🚀 Sprint 1 — Importação dos dados

A primeira etapa consiste na leitura e inspeção da base.

Foi utilizado o `csv.DictReader` para realizar a extração estruturada dos registros e, posteriormente, os dados foram convertidos para um `DataFrame` do Pandas.

### Principais verificações

- Quantidade de registros;
- Quantidade de colunas;
- Nomes das colunas;
- Tipos de dados;
- Identificação de colunas completamente vazias.

### Resultado inicial

```text
Registros originais: 830.000
Colunas originalmente presentes: 14
Colunas úteis após inspeção: 10
```

As quatro colunas completamente vazias foram removidas por não apresentarem informações para a análise.

---

## 🧹 Sprint 2 — Transformação e padronização

Nesta etapa foram realizadas transformações necessárias para melhorar a consistência dos dados.

### 🔤 Tratamento de textos

As colunas textuais foram submetidas a procedimentos de padronização, incluindo remoção de espaços desnecessários e tratamento de marcadores de ausência de informação.

### 🔢 Conversão de tipos numéricos

As colunas identificadoras e a coluna utilizada para a análise do número de filhos foram convertidas para tipos numéricos apropriados:

```text
CO_ID
CL_ID
CL_FHL
PR_ID
```

### 📅 Conversão da data

A coluna `DATA` foi convertida para o tipo `datetime`.

Foi utilizada uma conversão com tratamento de possíveis valores inválidos:

```python
pd.to_datetime(..., dayfirst=True, errors="coerce")
```

Após a conversão, não foram identificadas datas inválidas.

### 📆 Período encontrado

A base apresenta registros entre **04/01/2019** e **08/12/2022**. Foram identificadas **333 datas distintas**.

---

## 🧹 Sprint 3 — Nulos e duplicatas

A análise de qualidade identificou dois pontos importantes:
- registros duplicados;
- categorias de produto sem classificação.

### 🔁 Registros duplicados

Na base original foram identificados **96.553 registros duplicados**, o que representa aproximadamente **11,63% da base original**. Os registros duplicados foram removidos para evitar distorções nas análises.

```text
830.000 registros  ➔  [ Remoção de duplicatas ]  ➔  733.447 registros
```

---

### 🏷️ Categorias sem classificação

Na coluna `PR_CAT`, foram encontrados registros com o marcador `#N/D`, que foram tratados como `Sem Categoria`. 

Após a remoção das duplicatas, permaneceram **3.228 registros** nessa condição, representando cerca de **0,44% da base limpa**.

---

### 🧪 Resultado da limpeza

| Indicador | Resultado |
| :--- | ---: |
| Registros originais | 830.000 |
| Duplicatas identificadas | 96.553 |
| Registros após remoção | 733.447 |
| Registros `Sem Categoria` | 3.228 |
| Datas inválidas | 0 |

---

## 📊 Sprint 4 — Estatística descritiva

A estatística descritiva foi realizada sobre a coluna `CL_FHL`, utilizada no projeto para representar o **número de filhos**.

| Estatística | Resultado |
| :--- | ---: |
| Contagem | 733.447 |
| Média | 1,1460 |
| Mediana | 0,0000 |
| Desvio padrão | 1,4169 |
| Moda | 0,0000 |
| Mínimo | 0,0000 |
| 1º quartil (Q1) | 0,0000 |
| 2º quartil (Q2) | 0,0000 |
| 3º quartil (Q3) | 2,0000 |
| Máximo | 4,0000 |

### 📌 Interpretação

A média indica aproximadamente **1,15 filho por registro**. Entretanto, a mediana e a moda são iguais a **0**, indicando que o valor mais frequente e o valor central da distribuição estão concentrados em clientes sem filhos registrados. O terceiro quartil é igual a **2**, enquanto o valor máximo encontrado é **4**.

---

## 📈 Sprint 5 — Agrupamentos e análise exploratória

Para explorar a estrutura da base e identificar padrões de consumo e perfil do cliente, foram realizados agrupamentos utilizando a função `groupby()`.

### 👥 Distribuição por Gênero (`CL_GENERO`)

| Gênero | Registros | Participação (%) |
| :---: | ---: | ---: |
| **F** | 382.427 | 52,14% |
| **M** | 351.020 | 47,86% |
| **Total** | **733.447** | **100,00%** |

### 🛒 Distribuição por Categoria de Produto (`PR_CAT`)

| Categoria | Registros | Participação (%) |
| :--- | ---: | ---: |
| **ALIMENTOS** | 384.197 | 52,38% |
| **HIGIENE** | 137.702 | 18,77% |
| **LIMPEZA** | 128.632 | 17,54% |
| **BEBIDAS** | 38.264 | 5,22% |
| **PET** | 28.553 | 3,89% |
| **ACESSORIOS** | 12.871 | 1,75% |
| **Sem Categoria** | 3.228 | 0,44% |
| **Total** | **733.447** | **100,00%** |

### 🏷️ Distribuição por Segmento (`CL_SEG`)

| Segmento | Registros | Participação (%) |
| :---: | ---: | ---: |
| **B** | 468.505 | 63,88% |
| **C** | 205.265 | 27,99% |
| **A** | 59.677 | 8,14% |
| **Total** | **733.447** | **100,00%** |

---

# 📋 Relatório Final da Análise (Console Output)

Abaixo está o relatório consolidado gerado automaticamente pela execução do pipeline de dados:

### 1. Volume de Dados
- **Registros originais:** 830.000
- **Registros após limpeza:** 733.447
- **Registros removidos como duplicados:** 96.553

---

### 2. Qualidade das Categorias
- **Registros sem categoria:** 3.228
- **Participação:** 0,44%

---

### 3. Estatísticas — Número de Filhos (`CL_FHL`)
| Métrica | Valor |
| :--- | :--- |
| **Contagem** | 733.447 |
| **Média** | 1,15 |
| **Mediana** | 0,00 |
| **Desvio padrão** | 1,4169 |
| **Mínimo** | 0 |
| **Q1 (25%)** | 0,00 |
| **Q2 (50%)** | 0,00 |
| **Q3 (75%)** | 2,00 |
| **Máximo** | 4 |
| **Moda** | 0 |

---

### 4. Principais Agrupamentos

#### 👥 Distribuição por Gênero (`CL_GENERO`)
| Gênero | Registros | Participação (%) |
| :---: | ---: | ---: |
| **F** | 382.427 | 52,14% |
| **M** | 351.020 | 47,86% |

#### 🛒 Distribuição por Categoria (`PR_CAT`)
| Categoria | Registros | Participação (%) |
| :--- | ---: | ---: |
| **ALIMENTOS** | 384.197 | 52,38% |
| **HIGIENE** | 137.702 | 18,77% |
| **LIMPEZA** | 128.632 | 17,54% |
| **BEBIDAS** | 38.264 | 5,22% |
| **PET** | 28.553 | 3,89% |
| **ACESSORIOS** | 12.871 | 1,75% |
| **Sem Categoria** | 3.228 | 0,44% |

#### 🏷️ Distribuição por Segmento (`CL_SEG`)
| Segmento | Registros | Participação (%) |
| :---: | ---: | ---: |
| **B** | 468.505 | 63,88% |
| **C** | 205.265 | 27,99% |
| **A** | 59.677 | 8,14% |

---

### 5. Período dos Dados
- **Datas válidas:** 733.447
- **Data inicial:** 04/01/2019 `00:00:00`
- **Data final:** 08/12/2022 `00:00:00`
- **Datas distintas:** 333
- **Datas ausentes ou inválidas:** 0

---

# 🔎 Principais insights

A Análise Exploratória de Dados (AED) realizada sobre a base higienizada permitiu extrair as seguintes observações estratégicas:

1. **Volume Significativo de Duplicidades:**
   - A limpeza identificou **96.553 registros duplicados**, o que representava cerca de **11,63% da base original**. A remoção dessas ocorrências foi crucial para evitar distorções nas métricas do negócio.

2. **Dominância da Categoria de Alimentos:**
   - A categoria **ALIMENTOS** lidera isoladamente com **52,38% do volume de compras** (384.197 registros). As categorias de **HIGIENE** (18,77%) e **LIMPEZA** (17,54%) ocupam o segundo e terceiro lugar, indicando que a base de clientes utiliza o estabelecimento majoritariamente para compras essenciais de abastecimento doméstico.

3. **Predominância do Segmento B:**
   - O **Segmento B representa 63,88% dos registros** (468.505 compras), seguido pelo Segmento C (27,99%) e Segmento A (8,14%). Isso sugere uma forte concentração no perfil intermediário de clientes, sendo o principal alvo para campanhas de fidelização.

4. **Equilíbrio na Distribuição de Gênero:**
   - O perfil de gênero mostra uma ligeira maioria de clientes do gênero **Feminino (F) com 52,14%**, enquanto o gênero **Masculino (M) representa 47,86%**. A proximidade entre os volumes indica um público comprador bastante equilibrado.

5. **Concentração Familiar na Faixa sem Filhos:**
   - A análise da variável `CL_FHL` revelou uma **média de 1,15 filhos por cliente**, com **mediana e moda iguais a 0**. Mais de metade da base (**52,49%**) não possui filhos registrados, enquanto 37,83% possuem entre 1 e 3 filhos.

6. **Integridade das Categorias e Registros:**
   - Os registros sem classificação de categoria (`#N/D`) representam apenas **0,44% da base limpa** (3.228 registros). A opção de imputação por `"Sem Categoria"` preservou o histórico das transações sem inventar atributos.

7. **Consistência Temporal e de Identificadores:**
   - O período analisado engloba **333 datas distintas entre 04/01/2019 e 08/12/2022**, com **100% de validação em identificadores de compra (`CO_ID`) e datas válidas**.

---

# 🔄 ETL aplicado ao projeto

O projeto também pode ser compreendido como um processo simplificado de **ETL — Extract, Transform, Load**.

```text
┌──────────────────────┐
│       EXTRACT        │
│                      │
│ Base Varejo.csv      │
│ csv.DictReader       │
│ Pandas               │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      TRANSFORM       │
│                      │
│ • Limpeza de textos  │
│ • Conversão de tipos │
│ • Datas → datetime   │
│ • Nulos              │
│ • Duplicatas         │
│ • Categorias         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│        LOAD          │
│                      │
│ DataFrame limpo      │
│ df_limpo.csv         │
│ Análises exploratórias│
└──────────────────────┘
```

### 🧠 Reflexão sobre o processo ETL

O processo demonstrou que a etapa de transformação é fundamental antes da análise. Uma base pode possuir grande quantidade de registros e, ainda assim, apresentar problemas que comprometem os resultados, como duplicidades, categorias sem classificação e tipos inadequados.

Por isso, a limpeza e a padronização foram realizadas antes dos cálculos estatísticos e agrupamentos.

---

# 📁 Estrutura do projeto

A organização do repositório está estruturada da seguinte forma:

```text
mini-projeto/
│
├── 📊 Base Varejo.csv
├── 📊 df_limpo.csv
├── 📓 Miniprojeto_Analise_Dados_Varejo.ipynb
└── 📄 README.md
```
---

# ▶️ Como executar o projeto

## 1. Clonar o repositório

Faça o clone do repositório do GitHub para a sua máquina local:

```bash
git clone https://github.com/carolinaruas-star/mini-projeto.git
```

---

## 2. Instalar as bibliotecas necessárias

Certifique-se de ter o Python 3 instalado e execute o comando abaixo no terminal para instalar as dependências utilizadas no projeto:

```bash
pip install pandas matplotlib
```

---

## 3. Verificar os arquivos da pasta

Certifique-se de que a base de dados bruta está salva na mesma pasta do notebook:

```text
mini-projeto/
├── 📊 Base Varejo.csv
└── 📓 Miniprojeto_Analise_Dados_Varejo.ipynb
```

---

## 4. Executar o Notebook

Você pode executar o projeto de duas formas:

### 💻 Opção A — Localmente (VS Code / Jupyter Notebook)
1. Abra a pasta `mini-projeto` no VS Code ou Jupyter Lab.
2. Abra o arquivo **`Miniprojeto_Analise_Dados_Varejo.ipynb`**.
3. Selecione o Kernel Python configurado.
4. Clique no menu superior em **Run All** (ou **Executar tudo**).

### ☁️ Opção B — Google Colab
1. Acesse o [Google Colab](https://colab.research.google.com/) e faça o upload do arquivo **`Miniprojeto_Analise_Dados_Varejo.ipynb`**.
2. Faça o upload do arquivo **`Base Varejo.csv`** no painel lateral de arquivos do Colab.
3. No menu superior, vá em **Ambiente de execução ➔ Executar tudo** (Ctrl + F9).

---

# 📤 Saídas geradas

Após a execução, o projeto disponibiliza:

- DataFrame com os dados tratados;
- diagnóstico da qualidade da base;
- informações sobre nulos;
- quantidade de duplicatas;
- estatística descritiva;
- agrupamentos;
- gráficos exploratórios;
- principais insights;
- arquivo final: `df_limpo.csv`

---

# 🧪 Qualidade dos dados

As principais decisões de tratamento foram documentadas para tornar o processo reproduzível.

| Problema | Tratamento |
| :--- | :--- |
| Colunas completamente vazias | Removidas |
| Registros duplicados | Removidos |
| `#N/D` em `PR_CAT` | Substituído por `Sem Categoria` |
| Datas em formato textual | Convertidas para `datetime` |
| Possíveis datas inválidas | Validadas durante a conversão |
| Identificadores | Convertidos para tipos numéricos |
| Textos | Padronizados com remoção de espaços |
| Dimensões físicas ausentes | Não aplicável à estrutura desta base |

### ⚠️ Observação importante

A base utilizada neste projeto não apresenta uma coluna monetária explícita entre os campos analisados. Portanto, não foram inventadas métricas de faturamento, ticket médio ou receita.

Da mesma forma, a atividade menciona tratamento de dimensões físicas, porém essas variáveis não estão presentes na estrutura efetivamente utilizada. Por isso, não foi realizada imputação artificial desses dados.

---

# 📚 Relação com as sprints

| Sprint | Aplicação no projeto |
| :--- | :--- |
| **Sprint 1 — Importação** | Leitura do CSV, `csv.DictReader`, DataFrame e inspeção inicial |
| **Sprint 2 — Transformação** | Strings, tipos numéricos e conversão de datas |
| **Sprint 3 — Nulos e duplicatas** | Tratamento de categorias sem classificação e remoção de duplicidades |
| **Sprint 4 — Estatística descritiva** | Análise da variável de número de filhos |
| **Sprint 5 — Relatório e documentação** | Insights, reflexão sobre ETL e documentação |
| **Sprint 6 — Versionamento** | Organização do código, README e base tratada para o GitHub |

---

# 🎯 Conclusão

A análise permitiu transformar uma base inicialmente composta por **830.000 registros** em uma base tratada com **733.447 observações**, após a remoção de registros duplicados e a aplicação das principais regras de limpeza.

A exploração também mostrou uma concentração significativa dos registros na categoria **ALIMENTOS**, no **segmento B** e uma distribuição de gênero relativamente equilibrada.

A análise estatística da variável de número de filhos mostrou média de aproximadamente **1,15**, enquanto mediana e moda permaneceram em **0**, indicando concentração de registros nessa faixa.

Além de produzir estatísticas e agrupamentos, o projeto reforça uma etapa essencial da análise de dados: **garantir a qualidade dos dados antes de utilizá-los para tomada de decisão**.

---

# ⚠️ Pontos de atenção e possíveis melhorias

Como continuidade do projeto, algumas análises poderiam ser exploradas futuramente:

- aprofundar a investigação dos identificadores de compra e cliente;
- analisar possíveis inconsistências cadastrais;
- explorar a evolução das compras ao longo do tempo;
- investigar relações entre segmentos, categorias e características dos clientes;
- criar um dashboard para visualização dos principais indicadores;
- ampliar as validações de qualidade dos dados.

---

# 💡 Aprendizados

Este mini-projeto permitiu praticar conceitos fundamentais de análise de dados com Python:

- leitura estruturada de arquivos CSV;
- manipulação de DataFrames;
- identificação de problemas de qualidade;
- tratamento de dados duplicados;
- tratamento de categorias sem informação;
- conversão de tipos;
- manipulação de datas;
- estatística descritiva;
- agrupamento de dados;
- geração de insights;
- organização de projetos para GitHub;
- documentação de processos de dados.

---

## 👩‍💻 Autora

**Ana Carolina Ruas**

Projeto desenvolvido como parte dos estudos em **Análise de Dados com Python**.

---

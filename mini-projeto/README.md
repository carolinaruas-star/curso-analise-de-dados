# 📊 Mini-Projeto Avaliativo — Análise de Dados com Python

**Turma:** `Analise_de_Dados_T1`
**Módulo:** 1 — Análise de Dados com Python
**Projeto:** Análise Exploratória de Dados de Varejo
**Status:** 🚧 Em desenvolvimento

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte do **Mini-Projeto Avaliativo do Módulo 1 — Análise de Dados com Python**, com o objetivo de aplicar, de forma prática, conceitos de **importação, transformação, limpeza, análise exploratória, estatística descritiva, agrupamentos e documentação de dados**.

A proposta consiste em trabalhar com uma base de registros de varejo, realizando um processo estruturado de preparação e exploração dos dados para identificar problemas de qualidade e obter informações úteis a partir da base.

O projeto busca transformar dados inicialmente brutos em uma estrutura mais organizada e adequada para análises posteriores, mantendo o processo **reprodutível, documentado e organizado**.

---

## 🎯 Objetivos

O projeto tem como principais objetivos:

* Importar e inspecionar uma base de dados de varejo;
* Identificar problemas de qualidade nos dados;
* Trabalhar com diferentes tipos de dados;
* Realizar transformações e padronizações;
* Identificar e tratar valores ausentes;
* Identificar e remover registros duplicados;
* Converter datas para o tipo adequado;
* Realizar estatística descritiva;
* Criar agrupamentos para análise exploratória;
* Extrair informações relevantes da base;
* Documentar as decisões tomadas durante o processo;
* Preparar uma base limpa para análises futuras.

---

## 🗂️ Base de dados

A base utilizada no projeto é:

```text
Base Varejo.csv
```

Após a leitura inicial, foram identificadas **830.000 linhas** e 14 colunas no arquivo original.

Durante a inspeção, foram identificadas **4 colunas completamente vazias**, decorrentes da estrutura do arquivo CSV. Essas colunas foram removidas por não apresentarem informações úteis para a análise.

Após essa etapa, foram consideradas as seguintes colunas:

| Coluna      | Descrição                                         |
| ----------- | ------------------------------------------------- |
| `DATA`      | Data da compra                                    |
| `CO_ID`     | Identificador da compra                           |
| `CL_ID`     | Identificador do cliente                          |
| `CL_GENERO` | Gênero do cliente                                 |
| `CL_EC`     | Campo cadastral do cliente                        |
| `CL_FHL`    | Número de filhos utilizado na análise estatística |
| `CL_SEG`    | Segmento do cliente                               |
| `PR_ID`     | Identificador do produto                          |
| `PR_CAT`    | Categoria do produto                              |
| `PR_NOME`   | Nome do produto                                   |

> **Observação:** o material fornecido não apresenta uma definição textual para todos os códigos das colunas. Por isso, o projeto evita atribuir significados que não estejam documentados na base ou no material da atividade.

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🐼 Pandas
* 📊 Matplotlib
* 📄 CSV
* 🔎 `csv.DictReader`
* 📓 Google Colab / VS Code
* 🌱 Git e GitHub

---

# 🔄 Processo de análise

O desenvolvimento foi organizado em etapas correspondentes às sprints propostas no projeto.

---

## 🚀 Sprint 1 — Importação dos dados

A primeira etapa consiste na leitura e inspeção da base.

Foi utilizado o `csv.DictReader` para realizar a extração estruturada dos registros e, posteriormente, os dados foram convertidos para um `DataFrame` do Pandas.

### Principais verificações

* Quantidade de registros;
* Quantidade de colunas;
* Nomes das colunas;
* Tipos de dados;
* Identificação de colunas completamente vazias.

### Resultado inicial

```text
Registros originais: 830.000
Colunas originalmente presentes: 14
Colunas úteis após inspeção: 10
```

As quatro colunas completamente vazias foram removidas por não apresentarem informações para a análise.

---

# 🧹 Sprint 2 — Transformação e padronização

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

A base apresenta registros entre:

```text
04/01/2019
        ↓
08/12/2022
```

Foram identificadas **333 datas distintas**.

---

# 🧹 Sprint 3 — Nulos e duplicatas

A análise de qualidade identificou dois pontos importantes:

* registros duplicados;
* categorias de produto sem classificação.

## 🔁 Registros duplicados

Na base original foram identificados:

```text
96.553 registros duplicados
```

Isso representa aproximadamente:

```text
11,63% da base original
```

Os registros duplicados foram removidos para evitar que a mesma observação fosse considerada mais de uma vez nas análises.

### Resultado após a remoção

```text
830.000 registros
        ↓
remoção de duplicatas
        ↓
733.447 registros
```

---

## 🏷️ Categorias sem classificação

Na coluna `PR_CAT`, foram encontrados registros com o marcador:

```text
#N/D
```

Esses valores foram tratados como:

```text
Sem Categoria
```

Essa decisão mantém os registros na base sem atribuir uma categoria que não está presente na fonte original.

Após a remoção das duplicatas, permaneceram:

```text
3.228 registros — Sem Categoria
```

Isso representa aproximadamente:

```text
0,44% da base limpa
```

---

## 🧪 Resultado da limpeza

| Indicador                 | Resultado |
| ------------------------- | --------: |
| Registros originais       |   830.000 |
| Duplicatas identificadas  |    96.553 |
| Registros após remoção    |   733.447 |
| Registros `Sem Categoria` |     3.228 |
| Datas inválidas           |         0 |

---

# 📊 Sprint 4 — Estatística descritiva

A estatística descritiva foi realizada sobre a coluna `CL_FHL`, utilizada no projeto para representar o **número de filhos**.

Foram calculadas as principais medidas solicitadas:

| Estatística     | Resultado |
| --------------- | --------: |
| Contagem        |   733.447 |
| Média           |    1,1460 |
| Mediana         |         0 |
| Desvio padrão   |    1,4169 |
| Moda            |         0 |
| Mínimo          |         0 |
| 1º quartil (Q1) |         0 |
| 2º quartil (Q2) |         0 |
| 3º quartil (Q3) |         2 |
| Máximo          |         4 |

### 📌 Interpretação

A média indica aproximadamente **1,15 filho por registro**.

Entretanto, a mediana e a moda são iguais a **0**, indicando que o valor mais frequente e o valor central da distribuição estão concentrados em clientes sem filhos registrados.

O terceiro quartil é igual a **2**, enquanto o valor máximo encontrado é **4**.

---

# 📈 Sprint 5 — Agrupamentos e análise exploratória

Para explorar a estrutura da base, foram realizados agrupamentos utilizando `groupby()`.

---

## 👥 Distribuição por gênero

| Gênero    |   Registros | Participação |
| --------- | ----------: | -----------: |
| F         |     382.427 |       52,14% |
| M         |     351.020 |       47,86% |
| **Total** | **733.447** |     **100%** |

### Insight

A distribuição apresenta uma participação ligeiramente maior do grupo identificado como `F`, correspondente a aproximadamente **52,14%** dos registros.

---

## 🛒 Distribuição por categoria de produto

| Categoria     |   Registros | Participação |
| ------------- | ----------: | -----------: |
| ALIMENTOS     |     384.197 |       52,38% |
| HIGIENE       |     137.702 |       18,77% |
| LIMPEZA       |     128.632 |       17,54% |
| BEBIDAS       |      38.264 |        5,22% |
| PET           |      28.553 |        3,89% |
| ACESSORIOS    |      12.871 |        1,75% |
| Sem Categoria |       3.228 |        0,44% |
| **Total**     | **733.447** |     **100%** |

### Insight

A categoria **ALIMENTOS** concentra mais da metade dos registros da base, representando aproximadamente **52,38%** das observações após a limpeza.

---

## 🏷️ Distribuição por segmento

| Segmento  |   Registros | Participação |
| --------- | ----------: | -----------: |
| B         |     468.505 |       63,88% |
| C         |     205.265 |       27,99% |
| A         |      59.677 |        8,14% |
| **Total** | **733.447** |     **100%** |

### Insight

O segmento **B** apresenta forte predominância na base, representando aproximadamente **63,88%** dos registros analisados.

---

# 🔎 Principais insights

A análise exploratória permitiu identificar os seguintes pontos:

* 🔁 **11,63% dos registros originais eram duplicados**, totalizando 96.553 ocorrências removidas durante a limpeza.
* 🛒 A categoria **ALIMENTOS representa 52,38%** da base após o tratamento dos dados.
* 🏷️ O **segmento B concentra 63,88%** dos registros analisados.
* 👥 O grupo identificado como **F representa 52,14%** dos registros, enquanto o grupo M representa 47,86%.
* 👶 A variável utilizada para representar o número de filhos apresenta **média de 1,15**, mas mediana e moda iguais a 0.
* ❓ Os registros classificados como **Sem Categoria representam apenas 0,44%** da base limpa.

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

O processo demonstrou que a etapa de transformação é fundamental antes da análise.

Uma base pode possuir grande quantidade de registros e, ainda assim, apresentar problemas que comprometem os resultados, como duplicidades, categorias sem classificação e tipos inadequados.

Por isso, a limpeza e a padronização foram realizadas antes dos cálculos estatísticos e agrupamentos.

---

# 📁 Estrutura do projeto

A organização sugerida para o repositório é:

```text
Miniprojeto_CarolinaRuas_Analise_de_Dados_T1/
│
├── 📄 README.md
├── 📓 Miniprojeto_Analise_Dados_Varejo.ipynb
├── 🐍 analise-dados-varejo.py
├── 📊 Base Varejo.csv
├── 📊 df_limpo.csv
│
└── 📁 imagens/
    └── fluxograma-etl.png
```

> A estrutura pode ser ajustada conforme os arquivos efetivamente utilizados na versão final do repositório.

---

# ▶️ Como executar o projeto

## 1. Clonar o repositório

Após disponibilizar o projeto no GitHub, clone o repositório para sua máquina.

## 2. Instalar as bibliotecas

```bash
pip install pandas matplotlib
```

## 3. Verificar os arquivos

Certifique-se de que a base de dados esteja disponível no mesmo diretório do código:

```text
Base Varejo.csv
```

## 4. Executar o projeto

No VS Code ou terminal:

```bash
python analise-dados-varejo.py
```

O projeto também pode ser executado em um ambiente como o **Google Colab**, utilizando o notebook disponibilizado no repositório.

---

# 📤 Saídas geradas

Após a execução, o projeto disponibiliza:

* DataFrame com os dados tratados;
* diagnóstico da qualidade da base;
* informações sobre nulos;
* quantidade de duplicatas;
* estatística descritiva;
* agrupamentos;
* gráficos exploratórios;
* principais insights;
* arquivo final:

```text
df_limpo.csv
```

---

# 🧪 Qualidade dos dados

As principais decisões de tratamento foram documentadas para tornar o processo reproduzível.

| Problema                     | Tratamento                           |
| ---------------------------- | ------------------------------------ |
| Colunas completamente vazias | Removidas                            |
| Registros duplicados         | Removidos                            |
| `#N/D` em `PR_CAT`           | Substituído por `Sem Categoria`      |
| Datas em formato textual     | Convertidas para `datetime`          |
| Possíveis datas inválidas    | Validadas durante a conversão        |
| Identificadores              | Convertidos para tipos numéricos     |
| Textos                       | Padronizados com remoção de espaços  |
| Dimensões físicas ausentes   | Não aplicável à estrutura desta base |

### ⚠️ Observação importante

A base utilizada neste projeto não apresenta uma coluna monetária explícita entre os campos analisados. Portanto, não foram inventadas métricas de faturamento, ticket médio ou receita.

Da mesma forma, a atividade menciona tratamento de dimensões físicas, porém essas variáveis não estão presentes na estrutura efetivamente utilizada. Por isso, não foi realizada imputação artificial desses dados.

---

# 📚 Relação com as sprints

| Sprint                                  | Aplicação no projeto                                                 |
| --------------------------------------- | -------------------------------------------------------------------- |
| **Sprint 1 — Importação**               | Leitura do CSV, `csv.DictReader`, DataFrame e inspeção inicial       |
| **Sprint 2 — Transformação**            | Strings, tipos numéricos e conversão de datas                        |
| **Sprint 3 — Nulos e duplicatas**       | Tratamento de categorias sem classificação e remoção de duplicidades |
| **Sprint 4 — Estatística descritiva**   | Análise da variável de número de filhos                              |
| **Sprint 5 — Relatório e documentação** | Insights, reflexão sobre ETL e documentação                          |
| **Sprint 6 — Versionamento**            | Organização do código, README e base tratada para o GitHub           |

---

# 🎯 Conclusão

A análise permitiu transformar uma base inicialmente composta por **830.000 registros** em uma base tratada com **733.447 observações**, após a remoção de registros duplicados e a aplicação das principais regras de limpeza.

A exploração também mostrou uma concentração significativa dos registros na categoria **ALIMENTOS**, no **segmento B** e uma distribuição de gênero relativamente equilibrada.

A análise estatística da variável de número de filhos mostrou média de aproximadamente **1,15**, enquanto mediana e moda permaneceram em **0**, indicando concentração de registros nessa faixa.

Além de produzir estatísticas e agrupamentos, o projeto reforça uma etapa essencial da análise de dados: **garantir a qualidade dos dados antes de utilizá-los para tomada de decisão**.

---

# ⚠️ Pontos de atenção e possíveis melhorias

Como continuidade do projeto, algumas análises poderiam ser exploradas futuramente:

* aprofundar a investigação dos identificadores de compra e cliente;
* analisar possíveis inconsistências cadastrais;
* explorar a evolução das compras ao longo do tempo;
* investigar relações entre segmentos, categorias e características dos clientes;
* criar um dashboard para visualização dos principais indicadores;
* ampliar as validações de qualidade dos dados.

> Essas possibilidades representam extensões futuras e não fazem parte dos resultados apresentados nesta etapa.

---

# 💡 Aprendizados

Este mini-projeto permitiu praticar conceitos fundamentais de análise de dados com Python:

* leitura estruturada de arquivos CSV;
* manipulação de DataFrames;
* identificação de problemas de qualidade;
* tratamento de dados duplicados;
* tratamento de categorias sem informação;
* conversão de tipos;
* manipulação de datas;
* estatística descritiva;
* agrupamento de dados;
* geração de insights;
* organização de projetos para GitHub;
* documentação de processos de dados.

---

## 👩‍💻 Autora

**Ana Carolina Ruas**

Projeto desenvolvido como parte dos estudos em **Análise de Dados com Python**.

---

## 📌 Status do projeto

🚧 **Projeto em desenvolvimento**

As etapas de análise, tratamento, estatística e documentação foram estruturadas de acordo com os requisitos do Mini-Projeto Avaliativo do Módulo 1.

**Próximas etapas:** revisão final, organização do repositório GitHub, versionamento dos arquivos e preparação da entrega.

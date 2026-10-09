# Sistema de Validação de Dados em Python

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema de validação de dados utilizando Python. O programa realiza a leitura de arquivos CSV, verifica informações por meio de expressões regulares (Regex), trata possíveis exceções e gera um relatório com os resultados obtidos.

Os dados analisados são e-mail, CPF, telefone e data.

## Tecnologias Utilizadas

- **Python:** linguagem principal do projeto.
- **CSV:** armazenamento e leitura dos registros.
- **Regex (`re`):** validação dos formatos dos dados.
- **Try/Except:** tratamento de erros durante a execução.
- **F-strings:** formatação dos relatórios.

## Validações Aplicadas

As validações foram implementadas para verificar se os dados seguem os padrões estabelecidos.

| Campo | Critério de validação |
|---|---|
| E-mail | Presença de usuário, `@` e domínio válido em formato. |
| CPF | Formato `000.000.000-00`. |
| Telefone | Sequência de 10 ou 11 dígitos. |
| Data | Formato `DD/MM/AAAA`. |

As expressões regulares utilizam metacaracteres como `\d`, `\w`, `^` e `$` para identificar os padrões.

Essas verificações contribuem para identificar registros incorretos e melhorar a organização dos dados.

As validações são estruturais, não incluindo a verificação matemática do CPF ou a existência real das datas.

## Tratamento de Exceções

Foram utilizados blocos `try`, `except`, `else` e `finally` para controlar possíveis falhas.

- **FileNotFoundError:** arquivo de dados não encontrado.
- **ValueError:** valor incompatível com uma conversão.
- **KeyError:** coluna obrigatória ausente no CSV.
- **FormatoInvalidoError:** exceção personalizada para dados que não atendem aos formatos exigidos.

O tratamento dessas exceções permite identificar problemas e apresentar mensagens adequadas, evitando encerramentos inesperados nas situações previstas.

## Exemplo de Entrada

Arquivo `dados.csv`:

```csv
email,cpf,telefone,data
joao@gmail.com,123.456.789-09,85999998888,10/05/2000
maria@gmail.com,987.654.321-00,85988887777,15/08/2002
emailerrado,12345,123,50/15/2020
```

## Exemplo de Saída

```text
========================================
         RELATÓRIO DE VALIDAÇÃO
========================================

Total de registros: 3
Registros válidos: 2
Registros inválidos: 1

--- DADOS VÁLIDOS ---

E-mail: joao@gmail.com
CPF: 123.456.789-09
Telefone: 85999998888
Data: 10/05/2000

E-mail: maria@gmail.com
CPF: 987.654.321-00
Telefone: 85988887777
Data: 15/08/2002

--- DADOS INVÁLIDOS ---

E-mail: emailerrado
CPF: 12345
Telefone: 123
Data: 50/15/2020

Percentual de válidos: 66.67%

========================================
```

## Resultados

A análise dos três registros demonstrou que:

- **3 registros** foram processados.
- **2 registros** atenderam aos padrões estabelecidos.
- **1 registro** apresentou informações inválidas.
- **66,67%** dos registros passaram na validação de formato.

O relatório permite visualizar os dados classificados e acompanhar as estatísticas da análise.

## Conclusão

O projeto demonstra a aplicação prática de conceitos fundamentais de Python, como manipulação de arquivos, expressões regulares, tratamento de exceções e formatação de saídas.

A implementação dessas funcionalidades contribui para a organização, a identificação de inconsistências e a automatização da análise de dados.

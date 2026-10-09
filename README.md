# entregavel_semana_5
# Sistema de Validação de Dados em Python

## 1. Descrição do Projeto

Este projeto foi desenvolvido em Python com o objetivo de ler um arquivo CSV contendo informações de usuários, validar os dados utilizando expressões regulares (Regex), tratar possíveis erros e gerar um relatório final com os resultados.

O sistema verifica quatro informações: e-mail, CPF, telefone e data.

## 2. Tecnologias Utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **CSV:** formato de arquivo utilizado para armazenar os dados.
- **Módulo `csv`:** responsável pela leitura dos registros.
- **Módulo `re`:** utilizado para validar os formatos por meio de expressões regulares.
- **F-strings:** utilizadas para formatar a apresentação dos resultados.

## 3. Validações Aplicadas

As validações foram criadas para identificar informações que não seguem os formatos esperados.

| Campo | Validação |
|---|---|
| E-mail | Verifica se possui nome, `@` e domínio. |
| CPF | Verifica o formato `000.000.000-00`. |
| Telefone | Verifica se possui 10 ou 11 dígitos. |
| Data | Verifica o formato `DD/MM/AAAA`. |

As expressões regulares utilizam metacaracteres como `\d`, `\w`, `^` e `$` para identificar padrões.

**Justificativa:** essas validações ajudam a evitar o processamento de dados com formatos incorretos, melhorando a organização e a confiabilidade dos registros.

**Limitação:** a validação verifica apenas o formato. Ela não confirma os dígitos verificadores do CPF nem se uma data existe no calendário.

## 4. Tratamento de Exceções

O programa utiliza `try`, `except`, `else` e `finally` para lidar com possíveis erros durante sua execução.

- **FileNotFoundError:** ocorre quando o arquivo CSV não é encontrado.
- **ValueError:** ocorre quando um valor não pode ser convertido para o tipo esperado.
- **KeyError:** ocorre quando uma coluna necessária não existe no arquivo CSV.
- **FormatoInvalidoError:** exceção personalizada utilizada para identificar informações que não atendem às regras de validação.

O bloco `else` executa quando não ocorre nenhuma exceção, enquanto o `finally` é executado independentemente do resultado.

Esses tratamentos permitem apresentar mensagens de erro mais claras e facilitar a identificação de problemas.

## 5. Exemplo de Entrada

O programa utiliza um arquivo chamado `dados.csv`, com o seguinte conteúdo:

```csv
email,cpf,telefone,data
joao@gmail.com,123.456.789-09,85999998888,10/05/2000
maria@gmail.com,987.654.321-00,85988887777,15/08/2002
emailerrado,12345,123,50/15/2020
```

O arquivo contém três registros, sendo dois com formatos válidos e um com informações inválidas.

## 6. Exemplo de Saída

Após a leitura e a validação, o sistema apresenta um relatório:

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

## 7. Como Executar

1. Instale o Python no computador.
2. Crie o arquivo `dados.csv` com as informações dos usuários.
3. Coloque o arquivo CSV na mesma pasta do script Python.
4. Abra o terminal nessa pasta.
5. Execute o comando:

```bash
python relatorio.py
```

O programa realizará a leitura, verificará os formatos e apresentará o relatório no terminal.

Não é necessário instalar bibliotecas externas, pois os módulos `csv` e `re` já fazem parte do Python.

## 8. Conclusão

O desenvolvimento deste projeto permitiu aplicar conhecimentos de leitura de arquivos, expressões regulares, tratamento de exceções e formatação de relatórios em Python.

A utilização dessas funcionalidades ajuda a tornar o código mais organizado, facilita a identificação de erros e demonstra como automatizar a verificação de informações cadastradas.

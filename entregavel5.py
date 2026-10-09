#script principal
import csv

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(f"E-mail: {linha['email']}")
        print(f"CPF: {linha['cpf']}")
        print(f"Telefone: {linha['telefone']}")
        print(f"Data: {linha['data']}")
        print("------------------------")

#validação regex
import re

def validar_email(email):
    padrao = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(padrao, email))

def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.fullmatch(padrao, cpf))

def validar_telefone(telefone):
    padrao = r"^\d{10,11}$"
    return bool(re.fullmatch(padrao, telefone))

def validar_data(data):
    padrao = r"^\d{2}/\d{2}/\d{4}$"
    return bool(re.fullmatch(padrao, data))


print(validar_email("joao@gmail.com"))
print(validar_cpf("123.456.789-09"))
print(validar_telefone("85999998888"))
print(validar_data("10/05/2000"))

#tratamento exceções
import csv

try:
    with open("dados.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            email = linha["email"]
            cpf = linha["cpf"]

            # Exemplo de conversão numérica
            ano = int(linha["data"].split("/")[-1])

            print(f"E-mail: {email}")
            print(f"CPF: {cpf}")
            print(f"Ano: {ano}")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")

except ValueError:
    print("Erro: Valor inválido!")

except KeyError:
    print("Erro: Coluna não encontrada no CSV!")

else:
    print("Arquivo processado com sucesso!")

finally:
    print("Processamento finalizado!")

#exceções personalizadas
import re

class FormatoInvalidoError(Exception):
    pass


def validar_email(email):
    padrao = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"

    if not re.fullmatch(padrao, email):
        raise FormatoInvalidoError("E-mail inválido!")

    return True


try:
    email = input("Digite seu e-mail: ")

    validar_email(email)

except FormatoInvalidoError as erro:
    print(f"Erro: {erro}")

else:
    print("E-mail válido!")

#relatorio formatado
import csv
import re

validos = []
invalidos = []

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        email = linha["email"]
        cpf = linha["cpf"]
        telefone = linha["telefone"]
        data = linha["data"]

        email_ok = re.fullmatch(
            r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$", email
        )

        cpf_ok = re.fullmatch(
            r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf
        )

        telefone_ok = re.fullmatch(
            r"^\d{10,11}$", telefone
        )

        data_ok = re.fullmatch(
            r"^\d{2}/\d{2}/\d{4}$", data
        )

        if email_ok and cpf_ok and telefone_ok and data_ok:
            validos.append(linha)
        else:
            invalidos.append(linha)


total = len(validos) + len(invalidos)

print(f"\n{'=' * 40}")
print(f"{'RELATÓRIO DE VALIDAÇÃO':^40}")
print(f"{'=' * 40}")

print(f"\nTotal de registros: {total}")
print(f"Registros válidos: {len(validos)}")
print(f"Registros inválidos: {len(invalidos)}")

print(f"\n--- DADOS VÁLIDOS ---")

for pessoa in validos:
    print(f"E-mail: {pessoa['email']}")
    print(f"CPF: {pessoa['cpf']}")
    print(f"Telefone: {pessoa['telefone']}")
    print(f"Data: {pessoa['data']}")
    print("--------------------")

print(f"\n--- DADOS INVÁLIDOS ---")

for pessoa in invalidos:
    print(f"E-mail: {pessoa['email']}")
    print(f"CPF: {pessoa['cpf']}")
    print(f"Telefone: {pessoa['telefone']}")
    print(f"Data: {pessoa['data']}")
    print("--------------------")

if total > 0:
    percentual = (len(validos) / total) * 100
else:
    percentual = 0

print(f"\nPercentual de válidos: {percentual:.2f}%")
print(f"{'=' * 40}")
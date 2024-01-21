# Criando código que ira calcular os pagamentos

def calcular_inss(salario_bruto):
    # Calculando o salario bruto quando ele for:
    if salario_bruto <= 1100:
        return salario_bruto * 0.075
    elif 1100.01 <= salario_bruto <= 2203.048:
        return salario_bruto *0.09
    elif 2203.049 <= salario_bruto  <= 3305.22:
        return salario_bruto * 0.12
    elif 3305.23 <= salario_bruto <= 6433.57:
        return salario_bruto * 0.14
    else:
        return 751.99

def calcular_irrf(salario_liquido):
    # Calculando o salario liquido quando ele for:
    if salario_liquido <= 1900.98:
        return 0
    elif 1903.99 <= salario_liquido <= 2826.65:
        return (salario_liquido * 0.075) - 142.8
    elif 2826.66 <= salario_liquido  <= 3751.05:
        return (salario_liquido * 0.15) - 354.8
    elif 3751.06 <= salario_liquido <= 4664.68:
        return (salario_liquido * 0.225) - 636.13
    else:
        return (salario_liquido * 0.275) - 869.36

def calcular_hora_extra(salario_bruto, horas_extras):
    valor_hora = salario_bruto / 220
    adcional = valor_hora * 0.5
    return horas_extras * (valor_hora + adcional)

salario_bruto = float(input("Insira o salario bruto do trabalhador:  R$"))
horas_extras = int(input("Quantas horas extras trabalhadas no mês: "))

desconto_inss = calcular_inss(salario_bruto)

salario_liquido = salario_bruto - desconto_inss

desconto_irrf = calcular_irrf(salario_liquido)

provento_horas_extras = calcular_hora_extra(salario_bruto, horas_extras)

salario_final = salario_liquido + provento_horas_extras - desconto_irrf

print('\n*** Folha de salario ***')
print(f'Salario bruto: R$ {salario_bruto:.2f}')
print(f'Provento de Horas extras: R$ {provento_horas_extras:.2f}')
print(f'Descontos e INSS: R$ {desconto_inss:.2f}')
print(f'Descontos e IRRF: R$ {desconto_irrf:.2f}')
print('------------------------------------------')
print(f'Salario final: R$ {salario_final:.2f}')

import math

n1 = float(input('Quanto ganha por hora: '))
n2 = float(input('quantas horas são trabalhadas: '))

salario_bruto = n1 * n2

salario_bruto_arrendondado = math.floor(salario_bruto)

desconto_inss = salario_bruto * 0.11
desconto_imposto_de_renda = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

desconto_inss_arrendondado = math.floor(desconto_inss)
desconto_imposto_de_renda_arrendondado = math.floor(desconto_imposto_de_renda)
desconto_sindicato_arrendondado = math.floor(desconto_sindicato)

salario_liquido = salario_bruto - desconto_inss - desconto_imposto_de_renda - desconto_sindicato

salario_liquido_arrendondado = math.floor(salario_liquido)

print(f'''Salario bruto: {salario_bruto_arrendondado}, 
      Salario liquido: {salario_liquido_arrendondado},
      INSS: {desconto_inss_arrendondado},
      SINDICATO: {desconto_sindicato_arrendondado},
      imposto de renda: {desconto_imposto_de_renda_arrendondado}
    ''')


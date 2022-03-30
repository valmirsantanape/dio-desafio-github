imovel = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o valor do salário? '))
tempo = int(input('Total de parcelas  '))
vlparcelas = imovel/tempo


if vlparcelas <= salario * 0.3:
    print('Imóvel: R${:.2f} ;Salario: R${:.2f}; Valor das parcelas: R${:.2f} em {} meses'.format(imovel, salario, vlparcelas, tempo))
    print('Simulação aprovada!\n Você pode fazer seu financiamento. ')
else:
    print('Imóvel: R${:.2f} ;Salario: R${:.2f}; Valor das parcelas: R${:.2f} em {} meses'.format(imovel, salario, vlparcelas, tempo))
    print('Simulação negada. \n O valor das parcelas excede o limite de 30% seu salário. ')
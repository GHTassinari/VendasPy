# Esse código foi utilizado no Google Colab
cUnitario = 20
despesasGerais = 1000
margemLucro = 0.1
quantidadeVendas = 60
quantidadeProduzida = 60

custosProducao = quantidadeProduzida * cUnitario
totalDespesas = custosProducao + despesasGerais
precoFinal = (totalDespesas/quantidadeProduzida) * (1 + margemLucro)
receitas = quantidadeVendas * precoFinal
lucro = receitas - totalDespesas

print(lucro)


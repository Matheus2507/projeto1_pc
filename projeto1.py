import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_br.UTF-8')
#ENTRADAS
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte mensa: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual (%)')) / 100
perc_cdb = float(input('Percentual do CDI (%)')) / 100
perc_lci = float(input('Percentual do LCI (%) ')) / 100
taxa_fii = float(input('Rentabilidade do FII (%) ')) /100
meta = float(input('Meta financeira (R$) '))

#CONVERSAO CDI
cdi_mensal = math.pow((1+ cdi_anual), 1/12) -1

#TOTAL INVESTIDO
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+ taxa_cdb), meses) + (aporte * meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses) + (aporte * meses))

#POPANÇA
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1 + taxa_poupanca), meses) + (aporte * meses))

#FII - SIMULAÇÕES 

montante_fii = (capital * math.pow((1 + taxa_fii), meses)+ (aporte * meses))
vari1 = montante_fii + random.uniform(-0.03, 0.03) * montante_fii
vari2 = montante_fii + random.uniform(-0.03, 0.03) * montante_fii
vari3 = montante_fii + random.uniform(-0.03, 0.03) * montante_fii
vari4 = montante_fii + random.uniform(-0.03, 0.03) * montante_fii
vari5 = montante_fii + random.uniform(-0.03, 0.03) * montante_fii


media_fii = statistics.mean((vari1 , vari2, vari3, vari4, vari5))
mediana_fii = statistics.median((vari1 , vari2, vari3, vari4, vari5))
desvio_fii = statistics.stdev((vari1 , vari2, vari3, vari4, vari5))

#DATAS
data_atual = datetime.datetime.now()
data_final = data_atual + datetime.timedelta(days = meses * 30)

#GRAFICO
barra_cdb = int(montante_cdb_liquido/1000)
barra_poupanca = int(montante_poupanca/1000)
barra_lci = int(montante_lci/1000)
barra_fii = int(media_fii/1000)

print(f'Data de hoje: {data_atual.strftime('%d/%m/%Y')}')
print(f'Data de resgate: {data_final.strftime('%d/%m/%Y')}')
print(f'total investido: {locale.currency(total_investido, grouping= True)}')

print(f'CDB{locale.currency(montante_cdb_liquido,grouping= True)}')
print(f'█'* barra_cdb)

print(f'LCI: {locale.currency(montante_lci,grouping=True)}')
print(f'█'* barra_lci)

print(f'Poupança: {locale.currency(montante_poupanca,grouping=True)}')
print(f'█'* barra_poupanca)

print(f'FII: {locale.currency(media_fii,grouping=True)}')
print(f'█' * barra_fii)
print(f'Media FII: {locale.currency(mediana_fii,grouping=True)}')
print(f'Desvio: {locale.currency(desvio_fii,grouping=True)}')

meta_final = max(montante_cdb_liquido,montante_lci,montante_poupanca,media_fii) >= meta
print(f'Meta atingida? {meta_final}')
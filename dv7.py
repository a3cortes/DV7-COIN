# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-

import requests

Bitcoin_en_satoshis = 100000000

info_mercados = requests.get("https://api.crypto-bridge.org/api/v1/ticker")
info_mercados = info_mercados.json()
valor_dv7_en_btc = info_mercados['DEV_BTC']['last']

info_btc = requests.get("https://api.coinmarketcap.com/v1/ticker/")
info_btc = info_btc.json()
valor_bitcoin_en_dolares = info_btc[0]['price_usd']
valor_bitcoin_en_dolares = float(valor_bitcoin_en_dolares)

valor_dolar_colombia = requests.get("https://www.datos.gov.co/resource/g3ab-sax9.json?$order=vigenciadesde DESC&$limit=1")
valor_dolar_colombia = valor_dolar_colombia.json()
valor_dolar_colombia = valor_dolar_colombia[0]['valor']
valor_dolar_colombia = float(valor_dolar_colombia) 

print '\n'
print "El valor de DV7Coin es: ", valor_dv7_en_btc, "Satochis  en el exchange: crypto-bridge" +'\n' 
print "Valor bitcoin hoy   es: ", format(valor_bitcoin_en_dolares,",.0f"), "Dolares" +'\n'
print "Valor del dolar hoy es: ", format(valor_dolar_colombia,",.2f"), "pesos colombianos" +'\n'
calculo_valor_BTC_en_pesos = valor_bitcoin_en_dolares * valor_dolar_colombia
print "Un Bitcoin  hoy cuesta: ", format(calculo_valor_BTC_en_pesos,",.0f"), "pesos colombianos" +'\n'
print '\n'
cuantos_satoshis = int(input("Escribe la cantidad de monedas DV7Coin a calcular:") )
calculo_monedas_en_satochis = (float(cuantos_satoshis) * float(valor_dv7_en_btc))
calculo_en_pesos = (calculo_monedas_en_satochis * calculo_valor_BTC_en_pesos)
calculo_en_dolares = (calculo_monedas_en_satochis * valor_bitcoin_en_dolares)
print '\n'
print format(cuantos_satoshis,",.0f") ,"monedas de DV7Coin son: $", format(calculo_en_pesos, ",.0f"), "Pesos Colombianos" +'\n'
print format(cuantos_satoshis,",.0f") ,"monedas de DV7Coin son: $", format(calculo_monedas_en_satochis,",.8f"), "Satochis" +'\n'
print format(cuantos_satoshis,",.0f") ,"monedas de DV7Coin son: $", format(calculo_en_dolares,",.6f"), "Dolares" +'\n'

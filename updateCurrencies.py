# -*- coding: utf-8 -*-
import sys
import requests

currenciesTemplateFile = open('./units/__currencyTemplate.py', 'r')
currenciesTemplate = currenciesTemplateFile.read().decode('utf-8')

rawResponse = requests.get('http://api.fixer.io/latest?base=USD')
response = rawResponse.json()

for currencyName, exchangeRate in response['rates'].iteritems():
    replaceFrom = "'{}!'".format(currencyName)
    exchangeRateToBaseCurrency = float(exchangeRate)
    exchangeRateFromBaseCurrency = 1 / exchangeRateToBaseCurrency
    replaceTo = unicode(exchangeRateFromBaseCurrency)
    currenciesTemplate = currenciesTemplate.replace(replaceFrom, replaceTo)

currenciesTemplate += """\n# DO NOT ALTER THIS FILE. IT IS DYNAMICALLY GENERATED BY ../updateCurrencies.py
# ALTER __currencyTemplate.py
"""

currenciesTemplate = currenciesTemplate.encode('utf-8')

if currenciesTemplate.find('!') != -1:
    print currenciesTemplate
    sys.exit(1)

currencyFile = open('./units/currency.py', 'w')
currencyFile.write(currenciesTemplate)

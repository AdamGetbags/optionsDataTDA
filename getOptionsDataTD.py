# -*- coding: utf-8 -*-
"""
TD API Option Data - Full Guide
@author: https://github.com/alexgolec/tda-api
shout out to Part Time Larry!!!
"""

from tda import auth, client
import json
import pandas as pd
from datetime import datetime, date
import TDAsecrets

try:
    c = auth.client_from_token_file(TDAsecrets.token_path, TDAsecrets.api_key)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, TDAsecrets.api_key, TDAsecrets.redirect_uri,
            TDAsecrets.token_path)

#get call options
# r = c.get_option_chain(symbol = 'XOM',
                        # contract_type = c.Options.ContractType.CALL)
# 
#get put options
# r = c.get_option_chain(symbol = 'XOM',
                        # contract_type = c.Options.ContractType.PUT)

#get all options
r = c.get_option_chain(symbol = 'XOM',
                        contract_type = c.Options.ContractType.ALL)

#dictionary keys
# print(r.json().keys())

#symbol 
# print(r.json()['symbol'])

#underlying price
# print(r.json()['underlyingPrice'])

#number of contracts
# print(r.json()['numberOfContracts'])

#option data
# print(json.dumps(r.json()['putExpDateMap'], indent=4))
# print(json.dumps(r.json()['callExpDateMap'], indent=4))

#all expirations
# print(r.json()['callExpDateMap'].keys())

#specific expiration
# print(list(r.json()['callExpDateMap'].keys())[0])

#all strike prices of specific expiration cycle
# print(r.json()['callExpDateMap'][
        # list(r.json()['callExpDateMap'].keys())[0]].keys())

#strike price
# print(list(r.json()['callExpDateMap'][
        # list(r.json()['callExpDateMap'].keys())[0]].keys())[0])

#dictionary of contract specific data for CALLS
# print(json.dumps(r.json()['callExpDateMap'][
# specific expiration
        # list(r.json()['callExpDateMap'].keys())[0]][
# specific strike
        # list(r.json()['callExpDateMap'][
        # list(r.json()['callExpDateMap'].keys())[0]].keys())[0]][0], indent = 4))

#get all options with specific strike price width around spot price
# ie. strike_count = 10; 5 strikes above, 5 below; 
# r = c.get_option_chain(symbol = 'XOM',
                        # contract_type = c.Options.ContractType.ALL,
                        # strike_count = 10)

#check strike price range
# print(r.json()['putExpDateMap'][
       # list(r.json()['putExpDateMap'].keys())[0]].keys())

#vertical options spreads
# r = c.get_option_chain(symbol = 'XOM',
#                         contract_type = c.Options.ContractType.ALL,
                        # strategy = c.Options.Strategy.VERTICAL,
                        # interval = 2)   
                        
#monthly strategy list keys
# print(r.json()['monthlyStrategyList'][0].keys())
#number of expirations (for verticals)
# print(len(r.json()['monthlyStrategyList']))
#DTE
# print(r.json()['monthlyStrategyList'][4]['daysToExp'])

#front expiration spread data 
# print(json.dumps(
       # r.json()['monthlyStrategyList'][0]['optionStrategyList'], indent=4))

#future expiration spread data
# print(json.dumps(
       # r.json()['monthlyStrategyList'][4]['optionStrategyList'], indent=4)) 

#covered options spreads
# r = c.get_option_chain(symbol = 'XOM',
                        # contract_type = c.Options.ContractType.ALL,
                        # strategy = c.Options.Strategy.COVERED)       

#single strike per expiration in r.json()['call/putExpDateMap']
# r = c.get_option_chain(symbol = 'XOM',
                        # contract_type = c.Options.ContractType.ALL,
                        # strike = 80)  

#month specific expirations
# r = c.get_option_chain(symbol = 'XOM',
                        # contract_type = c.Options.ContractType.ALL,
                        # exp_month = c.Options.ExpirationMonth.APRIL)  

# datetime object
# dt = datetime(2022, 6, 9)

#expirations after a specific date
# r = c.get_option_chain(symbol = 'XOM',
                        # contract_type = c.Options.ContractType.ALL,
                        # from_date = dt) 
 
# expirations before a specific date
# r = c.get_option_chain(symbol = 'XOM',
                        # contract_type = c.Options.ContractType.ALL,
                        # to_date = dt) 
                        
#JSON to dataframe
assert r.status_code == 200, r.raise_for_status()
print(json.dumps(r.json(), indent = 4))

#checking for correct month expirations
# print(r.json()['putExpDateMap'].keys())

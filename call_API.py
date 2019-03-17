from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data

def getVolume(entity, time):
    f = get_historical_data(entity, token='sk_cbd784c0dc49477f8b34c194baf68b89')
    #print(f)
    print(f.loc[time]['volume'])
    return f.loc[time]['volume']

def getValue(entity, intent, time):
    try:
        ent = Stock(entity, token='sk_cbd784c0dc49477f8b34c194baf68b89')
        if intent == "real_time_price":
            return "the real time price of the target company is {0}".format(ent.get_price())
        elif intent == "volume_of_transactions":
            print("getValue", time)
            return "the volume of transaction in that day of target ORG is {0}".format(getVolume(entity, time))
        elif intent == "market_capitalization":
            return "the total market_capitalization of target ORG is {0}".format(ent.get_market_cap())
        else:
            return "sorry, i don't know, any other questions?"
    except:
        return "sorry, i don't know, any other questions?"

#aapl=Stock('AAPL',token='sk_cbd784c0dc49477f8b34c194baf68b89')
#aapl.getValue()
#getValue('TSLA', 'volume_of_transactions', '2019-02-12')
from iexfinance.stocks import Stock

def getValue(entity, intent):
    try:
        ent = Stock(entity, token='sk_cbd784c0dc49477f8b34c194baf68b89')
        if intent == "real_time_price":
            return ent.get_price()
        elif intent == "volume_of_transactions":
            return ent.get_volume()
        elif intent == "market_capitalization":
            return ent.get_market_cap()
        else:
            return "sorry, i don't know!"
    except:
        return "sorry, i don't know!"

#aapl=Stock('AAPL',token='sk_cbd784c0dc49477f8b34c194baf68b89')
#aapl.get_price()
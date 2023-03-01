import kiteSettings
from kiteconnect import kiteConnect


def quoteMethod(symbol):
	kite = kiteConnect(kiteSettings.api_key)
	kite.set_access_token(kiteSettings.access_token)

	quoteDetails = kite.quote(symbol)

	return quoteDetails



symbol = "NSE:INFY"

details = quoteMethod(symbol)

print(details)
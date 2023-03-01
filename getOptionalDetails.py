import kiteSettings
from kiteconnect import kiteConnect


def getQuote(instrumentCode):
	kite = kiteConnect(kiteSettings.api_key)
	kite.set_access_token(kiteSettings.access_token)
	inst_dictionary = kite.quote(instrumentCode)

	return inst_dictionary


if __name__ == "__main__":
	instrumentCode = "NFO:NIFTY"
	optionData = getQuote(instrumentCode)
	print(optionData)

# print("Last price",inst_dictionary[instrumentCode]['last_price'])
import kiteSettings
from kiteconnect import kiteConnect
import csv
import time

def writeCSV(data):
	with open('RecordData.csv','a',newline='') as ofile:
		writer = csv.writer(ofile)
		writer.write(data)

def getQuote(instrumentCode):
	kite = kiteConnect(kiteSettings.api_key)
	kite.set_access_token(kiteSettings.access_token)
	inst_dictionary = kite.quote(instrumentCode)

	return inst_dictionary

def run():
	instrumentCode = "NFO:NIFTY"
	optionData = getQuote(instrumentCode)
	print(optionData)
	dttime = optionData[instrumentCode]['timestamp']
	oi = optionData[instrumentCode]['oi']
	last_price = optionData[instrumentCode]['last_price']

	data = [dttime.strftime(),oi,last_price]

	writeCSV(data)

if __name__ == "__main__":
	for x in range(10000):
		try:
			run()
			time.sleep(5)
		except:
			print("Connection failed")
			time.sleep(5)
			pass
		print("--------------")

# print("Last price",inst_dictionary[instrumentCode]['last_price'])
import logging
import kiteSettings
from kiteconnect import kiteConnect

logging.basicConfig(level=logging.DEBUG)

kite = kiteConnect(kiteSettings.api_key)

request_token = input("Request token: ")

data = kite.generate_session(request_token,kiteSettings.api_secret)

kite.set_access_token(data["access_token"])


print("=================")

print("Access Token: ",data["access_token"])
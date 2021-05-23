from twilio.rest import Client
import requests
import json
import config

client = Client(config.account_sid, config.auth_token)

response = requests.get("https://api.quotable.io/random")
response_dict = json.loads(response.text)
while config.keyword in response_dict["author"]:
    response = requests.get("https://api.quotable.io/random")
    response_dict = json.loads(response.text)
send = "\"{}\"\n- *{}*".format(response_dict["content"], response_dict["author"])
client.messages.create(body=send, from_=config.send_to, to=config.send_from)

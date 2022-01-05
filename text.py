from twilio.rest import Client

account_sid = "AC2c251c61364b6b1f62929b512888868e"

auth_token = "0ee267ef23291a7cfa98a9c890b9e4f8"
# +14433314396

client = Client(account_sid, auth_token)

message = client.messages.create(
	to = "+88691234567",
	from_ = "+14433314396",
	body = "今天好嗎？")

print(message.sid)
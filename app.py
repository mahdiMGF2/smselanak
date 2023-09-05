import requests

# data send message to panel
username = "**username**" # username panel
password = "**password**" # password panel
fromNum = "**number**" # number for send message
toNum = input("Send the recipient's mobile number : ") # The recipient's number
Content = input("Submit the text : ") # text message
Type  = "0" # type send message [0,1] 


sms = requests.get(f"http://payammatni.com/webservice/url/send.php?method=sendsms&format=json&from={fromNum}&to={toNum}&text={Content}&type={Content}&username={username}&password={password}").text
print(sms)

import json
import requests
import datetime
from requests.auth import HTTPBasicAuth
from base64 import b64encode


def Oauth():
	consumer_key = "0wwptuTgw81A4a5k4KxGhsV1Ukd1S3id"
	consumer_secret = "IAoJNhAOmiq94UNo"
	api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
	r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
	return json.loads(r.text)
	

def mpesaTransact(amount,phone,orderId):
    paybill='174379'
    shortcode='603031'
    LipaNaMpesaPasskey='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    timestamp=datetime.datetime.now().strftime("%Y%m%d%I%M%S")
    access_token=Oauth()
 

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = { "Content-Type":"application/json","Authorization": "Bearer %s" % access_token['access_token'] }

    pass1="%s%s%s"%(paybill,LipaNaMpesaPasskey,timestamp)
    request = {
    "BusinessShortCode": paybill,
    "Password":  b64encode(pass1.encode()).decode(),
    "Timestamp": timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": amount,
    "PartyA": shortcode,
    "PartyB": paybill,
    "PhoneNumber":phone,
    "CallBackURL": "https://39798022.ngrok.io/kamaathe/callback.py",
    "AccountReference":orderId,
    "TransactionDesc": "test"
    }
    response = requests.post(api_url,json=request, headers=headers)
    return response.text

# respo=json.loads(mpesaTransact(10,'254727937153','QSWEDHJD'))
# if(respo.get('ResponseCode')):
#         print("success")
#         print(respo)

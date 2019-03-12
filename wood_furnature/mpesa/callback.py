#!C:/python/python.exe   
from mpesa import mpesaTransact
print('Content-type: text/html\r\n\r')


import sys,json

resp=json.loads(sys.stdin.read())['Body']['stkCallback']

MerchantRequestID = resp['MerchantRequestID']
CheckoutRequestID = resp['CheckoutRequestID']

if (resp['ResultCode'] == 0):
    metadata = resp['CallbackMetadata']['Item']
    amount = metadata[0]['Value']
    MpesaReceiptNumber = metadata[1]['Value']
    TransactionDate = metadata[3]['Value']#timestamp
    phoneNumber = metadata[4]['Value']
    #update status to paid
    print(' %s %s %s'%(amount,MpesaReceiptNumber,phoneNumber))

elif resp['ResultCode']==1032:
    print('cancelled %s'%MerchantRequestID)
    #cancel
elif resp['ResultCode']==1:
    #cancel
    
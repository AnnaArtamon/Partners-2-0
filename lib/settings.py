auth_headers = {"Authorization": "Basic dGVzdF9hcGk6MTIzNDU2",
                   "api_key": "13695c175a5646f68d647ca1cdc59be0"}

base_url = "http://vs-msk01-app01t/eapteka_t_artamonova2/hs/partners_api2_0/v2"

order_body = '''
{
   "orders":[
         {
         "customer":{
            "name":"Олег Котиков",
            "phone":"+79152956789",
            "email":"kotik@mail.ru"
         },
         "order_number": "00000780",
         "external_id":"4acc35b6-50a7-11eb-9370-005053870080",
         "date":"2021-08-31T16:02:46",
         "deliverypoint_id":"595FA0D8-F2C9-11EA-9972-D89EF37D77FA",
         "sum":1000,
         "positions":[
            {
               "product_id":"32ce7b00-f2b5-11ea-9972-d89ef37d77fa",
               "quantity":1,
               "price":1000,
               "nds":10
            }
         ],
         "payment":{
            "rrn":"62879193750",
            "transaction_id":"11111",
            "auth_code":"95F96T"
         }
      }
   ]
}
'''
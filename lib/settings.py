auth_headers = {"Authorization": "Basic 0JDRgNGC0LDQvNC+0L3QvtCy0LDQkDo=",
                   "api_key": "708b5069da82427894c6ae06d6fcbfd2"}

base_url = "http://vs-msk01-app01t:1841/erp_d03_sudarikov/hs/partners_api2_0/v2"

order_body = '''
{
   "orders":[
         {
         "customer":{
            "name":"Олег Котиков",
            "phone":"+79152956789",
            "email":"kotik@mail.ru"
         },
         "order_number": "me_94455078",
         "external_id":"4acc35b6-50a7-11eb-9370-005053870080",
         "date":"2022-01-18T16:02:46",
         "deliverypoint_id":"D6B71F29-C205-11EB-9E53-00505687D61D",
         "sum":1000,
         "positions":[
            {
               "product_id":"a6d4aacc-344a-4f50-98a5-8fa94e201d53",
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
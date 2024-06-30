
from woocommerce import API

wcapi = API(
    url="https://beautynani.com",
    consumer_key="ck_bb294b831c0039a8a57c2f8058f00ed389a",
    consumer_secret="cs_1fc1a20d24a8b235375a2aa01c9d56495823552",
    version="wc/v3"
)
r= wcapi.get("products")
r.encoding = 'UTF-8'
products = r.json()
print(products)
for res in products:
    print(res["name"])
    print(res['images'][0]['src'])
    print(res['price'])





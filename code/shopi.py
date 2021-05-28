# -*- coding: utf-8 -*-

import shopify
import sqlite3


def readDb():
    co = sqlite3.connect("database.db")
    cursor = co.cursor()
    query = "SELECT * FROM PRODUCTS"
    try:
        cursor.execute(query)
        co.commit()
        result = cursor.fetchall()
    except Exception as readDbError:
        print(readDbError)
        co.rollback()

    return result

def setVariables():
    data = readDb()
    for i in data:
        
        name = i[1].replace("buy","")
        name = name.replace("prices","")
        name = name.replace("-"," ")
        
        price = i[3]
        images = i[5].split("*")
        category = i[8]


API_KEY = "************"
PASSWORD = "***************"
SHARED_SECRET = "*******************"
shop_url = "https://%s:%s@cusprod.myshopify.com/admin" % (API_KEY, PASSWORD)
shopify.Session.setup(api_key=API_KEY, secret=SHARED_SECRET)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current

Produits = readDb()
i = 0
for produit in Produits:
    name = produit[1].replace("buy","")
    name = name.replace("prices","")
    name = name.replace("-"," ")
    price = produit[3]
    price = price.replace(",",".")
    images = produit[5].split("*")
    category = produit[8]
    i+= 1
    new_product = shopify.Product()
    new_product.title = name
    new_product.product_type = category
    new_product.vendor = "Cusprod"
    new_product.body_html = "<strong> {} :<br>{} </strong>".format(category,name)
    new_product.images = []
    for im in images:
        image = shopify.Image()
        image.src = im  
        new_product.images.append(image)
    
    
    new_product.options = []

    #red_variant = shopify.Variant({})
    blue_variant = shopify.Variant({"price":price})
    new_product.variants =  [blue_variant]
    #new_product.variants = [variant1, variant2]

    success = new_product.save()  # Sends request to Shopify
    print(success)
    print(str(i))
    
    




import json
from .models import Product
import requests

def clean_price(price_str):
    # Remove spaces and replace comma with dot for decimal separation
    cleaned_price = price_str.replace(' ', '').replace(',', '.')
    # Ensure it contains only numeric and dot characters
    cleaned_price = ''.join(filter(lambda x: x.isdigit() or x == '.', cleaned_price))
    return cleaned_price

def nurbek():
    with open('/home/chyngyz/Bekbekei/apps/products/response.json', 'r') as file:
        data = json.load(file)

        for i in data:
            price = i.get("price", "")  # Get the price or set to empty string if it doesn't exist
            if price:  # Check if price exists and is not an empty string
                cleaned_price = clean_price(str(price))
                obj = Product(
                    title=i["name"],
                    code=i["product_id"],
                    price=cleaned_price,
                    old_price=i["discounted_price"],
                    price_for=i["unit"],
                    quantity=i["quantity"]
                )
                obj.save()
            else:
                print('its ok')
                obj = Product(
                    title=i["name"],
                    code=i["product_id"],
                    price=0,
                    old_price=i["discounted_price"],
                    price_for=i["unit"],
                    quantity=i["quantity"]
                )
                obj.save()

        print(data)


        # print(data)
def update_products():
    url = 'http://31.186.48.247/Roznica/hs/MobileApp/product-list'
    headers = {"Authorization": 'Basic 0JDQtNC80LjQvdC40YHRgtGA0LDRgtC+0YA6'}
    response = requests.get(url=url, headers=headers)

    products_data = response.json()

    for product_data in products_data:
        product_id = product_data.get('product_id')
        name = product_data.get('name')
        price = clean_price(product_data.get('price'))  # Clean the price
        quantity = product_data.get('quantity')
        unit = product_data.get('unit')

        products = Product.objects.filter(code=product_id)
        if products.exists():
            for product in products:
                product.title = name
                product.price = float(price)
                product.quantity = quantity
                product.price_for = unit
                product.save()
        else:
            Product.objects.create(
                code=product_id,
                title=name,
                price=float(price),
                quantity=quantity,
                price_for=unit,
            )

def sms():
    # user = User.objects.get(phone=phone)
    xml_data = f"""<?xml version="1.0" encoding="UTF-8"?><message><login>nurbektmusic</login><pwd>Nuh020207</pwd><sender>SMSPRO.KG</sender><text>Список товаров обновлен!</text><phones><phone>996501774428</phone></phones></message>"""

    headers = {"Content-Type": "application/xml"}

    url = "https://smspro.nikita.kg/api/message"

    response = requests.post(url, data=xml_data.encode("utf-8"), headers=headers)

    # print(f"\n\n{response.text}\n\n")

    if response.status_code == 200:
        return True
    return False
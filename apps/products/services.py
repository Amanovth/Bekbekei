# import requests
# from django.conf import settings
# from apps.products.models import UnloadedProducts

# def unload_products(instance):
#     url = f"http://31.186.48.247/Roznica/hs/MobileApp/product-list?Guid={instance.cat.guid}"
#     headers = {"Authorization": settings.ONE_C}

#     response = requests.get(url=url, headers=headers)

#     product_list = response.json()

#     for product in product_list[:1]:
#         UnloadedProducts.objects.create(
#             cat=instance.cat,
#             name=product["name"],
#             product_id=product["product_id"],
#             barrcode=product["Barcode"],
#             price=product["price"],
#             discounted_price=product["discounted_price"],
#             quantity=product["quantity"],
#             unit=product["unit"]
#         )
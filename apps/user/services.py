from .models import User
from django.conf import settings
import requests


def send_sms(phone, message, code):
    # user = User.objects.get(phone=phone)
    new_phone = "".join(filter(str.isdigit, phone))
    xml_data = f"""<?xml version="1.0" encoding="UTF-8"?><message><login>{settings.NIKITA_LOGIN}</login><pwd>{settings.NIKITA_PASSWORD}</pwd><sender>{settings.NIKITA_SENDER}</sender><text>{message} {code}</text><phones><phone>{new_phone}</phone></phones></message>"""

    headers = {"Content-Type": "application/xml"}

    url = "https://smspro.nikita.kg/api/message"

    response = requests.post(url, data=xml_data.encode("utf-8"), headers=headers)

    # print(f"\n\n{response.text}\n\n")

    if response.status_code == 200:
        return True
    return False


def os_registration(user_id, user_card, firstname, lastname):
    url = settings.ONE_C_REG

    params = {
        "user_id": int(user_id),
        "user_card": user_card,
        "firstname": firstname,
        "lastname": lastname,
    }
    headers = {"Authorization": settings.ONE_C}
    response = requests.post(url, params=params, headers=headers)

    # print(f"\n\n1С says\n{response.text}\n\n")

    if response.status_code == 200:
        try:
            result = response.json().get("result")
            if result == "true":
                return True
        except Exception as e:
            print(f"Ошибка при обработке ответа: {e}")

    return False


def os_getbalance(user_id):
    url = settings.ONE_C_BAL

    params = {"user_id": user_id}

    headers = {"Authorization": settings.ONE_C}
    response = requests.get(url, params=params, headers=headers)

    # print(f"\n\n1С says\n{response.text}\n\n")

    if response.status_code == 200:
        balance_data = response.json()
        balance = balance_data["balance"]
        return f"{balance}"
    else:
        print("Не удалось получить баланс. Код состояния:", response.status_code)

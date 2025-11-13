import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

currency = input("Введіть валюту (EUR, USD, PLN): ").upper()
amount = float(input("Введіть кількість валюти: "))

rate = None  

# Перебираємо всі елементи
for elem in response.json():
    if elem["cc"] == "EUR" or elem["cc"] == "USD" or elem["cc"] == "PLN":
        print(elem)   # показуємо потрібні валюти
        
        # Якщо знайдена валюта користувача – беремо курс
        if elem["cc"] == currency:
            rate = elem["rate"]

# Конвертація
if rate is not None:
    result = amount * rate
    print(f"\n{amount} {currency} = {result:.2f} грн")
else:
    print("Такої валюти не знайдено у курсах НБУ.")

convert_amount = float(input())
exchange_rates = {"RUB": 2.98,"ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}
for currency, rate in exchange_rates.items():
    print(f'I will get {round(convert_amount * rate, 2)} {currency} from the sale of {convert_amount} conicoins.')

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="1", area="123", first="456", last="7890")
print(phone_num)

print()

phone_num = get_phone(country="91", area="835", first="689", last="4561")
print(phone_num)
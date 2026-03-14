from address import Address
from mailing import Mailing

address1 = Address("123456", "Москва", "Никольская ул.", 2, 40)
address2 = Address("987456", "Рязань", "ул. Ленина", 5, 8)
mailing = Mailing(to_address=address1, from_address=address2, cost=750, track="GT900")

print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. Стоимость {mailing.cost} рублей.")

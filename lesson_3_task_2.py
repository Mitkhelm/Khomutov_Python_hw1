from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy", 88005553535),  # Кто не пропел, тот - печенька.
    Smartphone("Nokia", "3310", 2741001),
    Smartphone("Электроника", "Дисковый", 2128506), # Для совсем уж динозавров
    Smartphone("Будка", "Автомат", 12345678),
    Smartphone("Xiaomy", "m987", +79262177508)
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}, {smartphone.number}")
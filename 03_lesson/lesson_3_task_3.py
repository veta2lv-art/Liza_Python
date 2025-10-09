from Mailing import Mailing
from Address import Address

add1 = Address("12345", "Moscow", "Gorshok", "2", "2")
add2 = Address("12345", "Moscow", "Pashok", "1", "1")
mail = Mailing(add1, add2, 4500, "QWERTY")
print("Отправление", mail.track, "из", mail.to_address.zip_code + ",",
      mail.to_address.city + ",", mail.to_address.street + ",",
      mail.to_address.building, "-", mail.to_address.apartment, "в",
      mail.from_address.zip_code + ",", mail.from_address.city + ",",
      mail.from_address.street + ",", mail.from_address.building, "-",
      mail.from_address.apartment + ".", "Стоимость", mail.cost, "рублей.")

from address import Address
from mailing import Mailing

to_address = Address("302001", "Орел", "Комсомольская", "53", "2")
from_address = Address("153000", "Иваново", "Ленина", "17", "10")

mailing = Mailing(to_address, from_address, 100, "45005145009749")

print(mailing)

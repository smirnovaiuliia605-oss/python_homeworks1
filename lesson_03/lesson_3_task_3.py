from address import Address
from mailing import Mailing

to_address = Address("456060", "Челябинск", "Ленина", "150", "15")
from_address = Address("456120", "Караганда", "Кирова", "15", "52")
cost = 125
track = "R1247852RU"

mailing = Mailing(to_address, from_address, 125, "R1247852RU")

print(mailing)

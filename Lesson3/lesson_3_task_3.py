from address import Address
from mailing import Mailing

address1 = Address("620026", "Екатеринбург", "Куйбышева", "48", "64")

address1.sayIndex()
address1.sayTown()
address1.sayStreet()
address1.sayHouse()
address1.sayFlat()

address2 = Address("110015", "Москва", "Большая Якиманка", 234, 15)

address2.sayIndex()
address2.sayTown()
address2.sayStreet()
address2.sayHouse()
address2.sayFlat()

mailing = Mailing(address1, address2, 1000, "ertyu34567")

mailing.sayToAddress()
mailing.sayFromAddress()
mailing.sayCost()
mailing.sayTrack()
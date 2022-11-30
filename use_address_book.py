import addressbook_pb2

person = addressbook_pb2.Person()

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PhoneType.HOME

phone2 = person.phones.add()
phone2.number = "555-4221"
phone2.type = addressbook_pb2.Person.PhoneType.MOBILE

print(person.__str__())



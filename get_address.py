#!/usr/bin/env python 

import addressbook_pb2
import sys 


# Iterates through all people in the AddressBook and prints info about them 
def ListPeople(address_book):
    
    for person in address_book.people:
        print(f"Person ID: {person.id}")
        print(f"    Name: {person.name}")

        if person.HasField('email'):
            print(f"    E-mail address: {person.email}")

        for phone_number in person.phones:
            match phone_number.type:
                case addressbook_pb2.Person.PhoneType.MOBILE:
                    print(f"    Mobile phone #: {phone_number.number}")
                case addressbook_pb2.Person.PhoneType.HOME:
                    print(f"    Home phone #: {phone_number.number}")
                case addressbook_pb2.Person.PhoneType.WORK:
                    print(f"    Work phone #: {phone_number.number}")


# Main procedure: Reads the entire address book from a file and prints all
#   the information inside 
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]}, [ADDRESS_BOOK_FILE]")
    sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

# Read the existing address book 
f = open(sys.argv[1], "rb")
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)
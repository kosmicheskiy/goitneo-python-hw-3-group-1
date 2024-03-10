from datetime import datetime, timedelta
from collections import UserDict
from classes import Field, Name, Phone, Birthday, Record, AddressBook
from get_birthdays import get_birthdays_per_week

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone/birthday please."
        except KeyError:
            return "User contacts was not found, try another user"
        except IndexError:
            return "Error occured, pls try again"
        except SyntaxError:
            return "Error occured, pls check spelling and try again"        

    return inner     

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error    
def add_contact(args, contacts):
        name, phone = args                 
        record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)
        return "Contact was added."

def hello():
    return "How can I help you?"

@input_error
def change_first_contact(contacts, name, phone):
    record = contacts.find(name)
    if (record != None):
        record.edit_phone(record.phones[0].value, phone)
        return "Contact was updated."
    else:
        return "Contact not found. Try to add contact first"

@input_error
def show_phone(contacts, name):
    record = contacts.find(name)
    if (record != None):
        return record.phones[0].value
    else:
        return "Contact not found. Try to add contact first"

@input_error
def show_all(contacts):
    if contacts.data:
        return "\n".join([str(record) for record in contacts.data.values()])
    else:
        return "Contacts were not found. Try to add contact first"
    
@input_error
def add_birthday(contacts, name, birthday):
    record = contacts.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."
    
@input_error
def get_birthday(contacts, name):
    record = contacts.find(name)
    if (record != None):
        return record.get_birthday()
    else:
        return "Contact not found. Try to add contact first"

@input_error
def print_birthdays_per_week(contacts):
    users = [{"name": name, "birthday": record.get_birthday()} for name, record in contacts.data.items()]
    return get_birthdays_per_week(users)

def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add" and len(args) >= 2:
            print(add_contact(args, contacts))
        elif command == "change" and len(args) == 2:
            print(change_first_contact(contacts, args[0], args[1]))
        elif command == "phone" and len(args) == 1:
            print(show_phone(contacts, args[0]))
        elif command == "all" and not args:
            print(show_all(contacts))
        elif command == "add-birthday" and len(args) == 2:
            print(add_birthday(contacts, args[0], args[1]))
        elif command == "show-birthday" and len(args) == 1:
            print(get_birthday(contacts, args[0]))
        elif command == "birthdays" and not args:
            results = print_birthdays_per_week(contacts)
        else:
            print("Invalid command.")
        
if __name__ == "__main__":
    main()

from collections import UserDict
from datetime import datetime, timedelta
from collections import defaultdict
from get_birthdays import get_birthdays_per_week

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Birthday(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        if(phone.isdigit() and len(phone) != 10):
            p = Phone(phone)
            self.phones.append(p)
        else:
            raise Exception("Pls check if phone is 10 digit number")

    def remove_phone(self, phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            print(f"{phone} was not found")
        
    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
            
        print(f"{phone} was not found")
        return None
    
    def add_birthday(self, birthday):
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid birthday format. Please use DD.MM.YYYY.")

        self.birthday = Birthday(birthday)

    def get_birthday(self):
        if(self.birthday != None):
            return self.birthday.value
        
        return None
                
    def __str__(self):
        phones = ', '.join([str(p.value) for p in self.phones])
        return f"Contact name: {self.name.value}, phones: {phones}; birthday:{self.birthday.value}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        users = [{"name": name, "birthday": record.get_birthday()} for name, record in self.data.items()]
        return get_birthdays_per_week(users)
    
    

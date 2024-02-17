from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        # перевірка на 10 символів і це цифри
        if len(value) != 10 or not value.isdigit():
            # якщо ValueError перериваємо програму і виводимо повідомлення
            raise ValueError("Phone number must contain 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # функція додавання телефону
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # функція видалення телефону
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    # функція редагування
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if str(phone) == old_phone:
                phone.value = new_phone
                break

    # функція пошуку за номером
    def find_phone(self, phone_number):
        for phone in self.phones:
            if str(phone) == phone_number:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones:{'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def find(self, name):
        if name in self.data:
            return self.data[name]


book = AddressBook()  # Створення нової адресної книги

john_record = Record("John")  # Створення запису для John
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


book.add_record(john_record)  # Додавання запису John до адресної книги

jane_record = Record("Jane")  # Створення та додавання нового запису для Jane
jane_record.add_phone("9876543210")
book.add_record(jane_record)


for name, record in book.data.items():
    print(record)  # Виведення всіх записів у книзі


john = book.find("John")  # Знаходження та редагування телефону для John
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

found_phone = john.find_phone("5555555555")  # Пошук конкретного телефону у записі John
print(f"{john.name}:{found_phone}")  # Виведення: 5555555555

book.delete("Jane")  # Видалення запису Jane

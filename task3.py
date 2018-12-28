import string
import random
import json

filename = "example.txt"
symbols_pass = string.ascii_letters + string.digits + '$%!_&'
number = 10

name_user = ['Aleksandr', 'Viktor', 'Denis', 'Petr', 'Dmitrii',
             'Fedor', 'Roman', 'Maksim', 'Nikita', 'Mikhail']

surname_user = ['Anisimov', 'Gazmanov', 'Fedorov', 'Zaytsev', 'Ivanov',
             'Lebedev', 'Suvorov', 'Engels', 'Sholohov', 'Morozova']

patronymic_user = ['Petrovich', 'Dmitryevna', 'Denisovich', 'Olegovich', 'Dmitrievich',
             'Fedorivich', 'Romanovich', 'Maksimovich', 'Nikitovich', 'Mikhailovich']

class Users:

    def __init__(self, name, surname, patronymic, passport, credit_card):

        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.passport = passport
        self.credit_card = credit_card
        self.password = ''.join(random.choice(symbols_pass)for _ in range(random.randint(6, 20)))
        self.login = ('' + name[0] + patronymic[0] + '.' + surname).lower()
        self.email = '' + self.login + '@gmail.com'

    def generator(self):
        Person = {
            'Name' : self.name,
            'Surname' : self.surname,
            'Patronymic' : self.patronymic,
            'Passport' : self.passport,
            'Credit_Card' : self.credit_card,
            'Password' : self.password,
            'Login' : self.login,
            'Email' : self.email
        }

        return Person

file_save = open(filename, mode='w')

for i in range(number):

    user = Users(
        random.choice(name_user),
        random.choice(surname_user),
        random.choice(patronymic_user),
        ''.join(random.choice(string.digits)for _ in range(10)),
        ''.join(random.choice(string.digits)for _ in range(12)))

    json.dump(user.generator(), file_save, indent=0)

file_save.close()






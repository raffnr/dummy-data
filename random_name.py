from faker import Faker
import random

fake = Faker('id_ID')

def generate_random_name():
    while True:
        name = fake.name()
        space = 0

        for j in range(len(name)):
            if name[j] == ' ':
                space+=1
    
        if space == 1:
            return name

def generate_instances():
    # Generating random name
    name = generate_random_name().split()
    firs_name = name[0]
    last_name = name[1]
    
    # Generating random email
    rand_int = random.randint(1, 999)
    if rand_int & 1 == 0:
        if rand_int >= 0 and rand_int <= 300:
            if ord(firs_name.lower()[0]) & 1 == 0:
                email = f'{firs_name.lower()}{last_name.lower()}{rand_int - ord(last_name[1])}@gmail.com'
            else:
                email = f'{firs_name.lower()}_{last_name.lower()}{rand_int}@outlook.com'
        elif rand_int > 300 and rand_int <= 700:
            if ord(firs_name.lower()[0]) & 1 == 0:
                email = f'{last_name.lower()}{firs_name.lower()}{rand_int}@gmail.com'
            else:
                email = f'{last_name.lower()}{firs_name.lower()}{rand_int}@outlook.com'

        else:
            if ord(firs_name.lower()[0]) & 1 == 0:
                email = f'{firs_name.lower()}{last_name.lower()}{last_name.lower()[len(last_name) - 1]}{rand_int}@outlook.com'
            else:
                email = f'{firs_name.lower()}{last_name.lower()}{last_name.lower()[len(last_name) - 1]}{rand_int}@gmail.com'
            
    else:
        if rand_int >= 0 and rand_int <= 300:
            if ord(firs_name.lower()[2]) & 1 == 0:
                email = f'{firs_name.lower()}_{last_name.lower()}{rand_int}@yahoo.com'
            else:
                email = f'{firs_name.lower()}_{last_name.lower()}{rand_int}@outlook.com'

        elif rand_int > 300 and rand_int <= 700:
            if ord(firs_name.lower()[2]) & 1 == 0:
                email = f'{firs_name.lower()}_{rand_int - ord(firs_name.lower()[1])}{ord(last_name[0])}@outlook.com'
            else:
                email = f'{firs_name.lower()}_{rand_int - ord(firs_name.lower()[1])}{ord(last_name[0])}@yahoo.com'

        else:
            if ord(firs_name.lower()[2]) & 1 == 0:
                email = f'{last_name.lower()}{rand_int - ord(firs_name.lower()[1])}{ord(firs_name[1])}@yahoo.com'
            else:
                email = f'{last_name.lower()}{rand_int - ord(firs_name.lower()[1])}{ord(firs_name[1])}@outlook.com'
            
        
    # Generate phone number
    phone = fake.phone_number()

    # Generate fake city
    city = fake.city()

    if city.lower()[0:17] == 'kota administrasi':
        city = city[18:]


    instance = (email, firs_name, last_name, city, phone)
    return instance


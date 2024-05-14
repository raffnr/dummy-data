from faker import Faker
import random

fake = Faker()

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
    rand_int = random.randint(1, 500)
    if rand_int & 1 == 0:
        email = f'{firs_name}{rand_int}@gmail.com'
    else:
        email = f'{firs_name}{rand_int}@yahoo.com'

    # Generate phone number
    phone = fake.phone_number()

    instance = (email, firs_name, last_name, phone)
    return instance


from models.customers import Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

fake = Faker()

for i in range(50):
    print("saving service",i+1,".......")
    a = randint(1990,2000)
    b = fake.name()
    new_customer = Customer(
        name = b,
        yob = a,
        gender = randint(0,1),
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        Status = choice([1,0]),
        email = b.replace(" ","") + str(a%100) + "@gmail.com" ,
        job = fake.job(),
        company = fake.company()
    )

    new_customer.save()


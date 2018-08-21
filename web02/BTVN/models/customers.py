from mongoengine import *

# design database
class Customer(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    Status = IntField()
    email = StringField()
    job = StringField()
    company = StringField()
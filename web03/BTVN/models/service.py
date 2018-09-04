from mongoengine import *

# design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    Status = BooleanField()
    image = StringField()
    description = StringField()
    measurements = ListField()
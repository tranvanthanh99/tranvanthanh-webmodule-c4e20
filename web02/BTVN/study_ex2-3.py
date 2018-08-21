from mongoengine import *
from models.service import Service
import mlab

mlab.connect()

a=Service.objects.get(id='5b7c5e5cf885d7288063e65f')

a.delete()
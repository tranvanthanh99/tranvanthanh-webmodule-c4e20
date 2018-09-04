from models.service import Service
import mlab

mlab.connect()
all_service = Service.objects()

f1 = all_service[0]
print(f1['id'])
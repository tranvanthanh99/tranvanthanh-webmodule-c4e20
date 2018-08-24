from models.service import Service
import mlab

mlab.connect()
all_service = Service.objects()

if len(all_service) > 0:
    all_service.delete()
    print("deleted")
else:
    print("Not Found")
from models.service import Service
import mlab

mlab.connect()
# all_service = Service.objects()

# first_service = all_service[0]

# print(first_service['name'])

id_to_find = "5b803c02f885d738a84be885"

# hera = Service.object(id=id_to_find)
# hera = Service.objects.get(id=id_to_find)
service = Service.objects.with_id(id_to_find)

if service is not None:
    # service.delete()
    # print("deleted")
    print("Before:")
    print(service['name'])
    service.update(set__yob=2005,set__name="link kute")
    service.reload()
    print("After:")
    print(service.to_mongo())
else:
    print("Not Found")
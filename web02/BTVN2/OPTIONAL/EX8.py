import mlab
from models.song import River

mlab.connect()
all_rivers = River.objects()

for river in all_rivers:
    if river['continent'] == 'Africa':
        print(river.to_mongo())
    
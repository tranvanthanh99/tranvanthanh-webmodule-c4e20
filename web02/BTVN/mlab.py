import mongoengine

# mongodb://user:Vantran297@ds127362.mlab.com:27362/muadongkhonglanhh

host = "ds127362.mlab.com"
port = 27362
db_name = "muadongkhonglanhh"
user_name = "user"
password = "Vantran297"


def connect():
    mongoengine.connect(
        db_name, 
        host=host, 
        port=port, 
        username=user_name, 
        password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
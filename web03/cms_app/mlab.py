import mongoengine

# mongodb://user:Vantran297@ds029595.mlab.com:29595/cms-app-c4e20

host = "ds029595.mlab.com"
port = 29595
db_name = "cms-app-c4e20"
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
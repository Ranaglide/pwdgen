from cryptography.fernet import Fernet
from os import getenv
from dotenv import load_dotenv
load_dotenv()



f = ""
try:
    key = getenv("db_key")
    if key:
        f = Fernet(bytes(key,"utf-8"))
    else:
        raise ValueError
except ValueError:
    print(Fernet.generate_key())


db_filename = "./db.rgld"

def get_all():
    data = ""
    with open(db_filename,"r",encoding="utf-8") as file:
        data = f.decrypt(file.read().encode("utf-8"))
    result = []
    for i in data.split("■".encode("utf-8")):
        params = i.split("∙".encode("utf-8"))
        result.append({
            "id":params[0].decode(),
            "host":params[1].decode(),
            "password":params[2].decode(),
            "lyrics":params[3].decode(),
            "album_id":params[4].decode(),
            "track_id":params[5].decode(),
        })
    return result

print(get_all())
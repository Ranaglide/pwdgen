from cryptography.fernet import Fernet
from os import getenv
from dotenv import load_dotenv
import uuid
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


def decode_info():
    data = ""
    with open(db_filename,"r",encoding="utf-8") as file:
        data = f.decrypt(file.read().encode("utf-8"))
    return data.decode()

def encode_info(data):
    with open(db_filename,"w",encoding="utf-8") as file:
        file.write(f.encrypt(data.encode("utf-8")).decode("utf-8"))
    return True

def generate_id():
    return str(uuid.uuid4())

def get_passwords():
    data = decode_info()
    passwords = []
    for i in data.split("■"):
        params = i.split("∙")
        passwords.append({
            "id":params[0],
            "host":params[1],
            "password":params[2],
            "lyrics":params[3],
            "album_id":params[4],
            "track_id":params[5]
        })
    return passwords





# encode_info('c9ef5ec3-46ff-4127-8e69-69dfa721468f∙google.com∙YfXfcf[JlybYekb∙На часах одни нули∙23756619∙105796954■af8e30a9-0ca1-4e9a-892d-0c70101d80b8∙google.com∙YfXfcf[JlybYekb∙На часах одни нули∙23756619∙105796954')
# print(decode_info())
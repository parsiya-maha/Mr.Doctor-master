import json
import PathVar
import jmespath
from make_hash import make_hash_from_str

def check_login_data_in_json(username:str,password:str):

    with open(PathVar.path_users_data) as F:
        data = json.load(F)

    usernames = jmespath.search("[*].username",data)
    passwords = jmespath.search("[*].password",data)
    
    password = make_hash_from_str(password)

    for u,p in zip(usernames,passwords):
        if [username,password] == [u,p]:
            return True
        
    return False


print(check_login_data_in_json("parsiya","1234"))
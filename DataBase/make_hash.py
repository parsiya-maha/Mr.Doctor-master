import hashlib

def make_hash_from_str(data:str):
    md5_hash = hashlib.md5(data.encode())
    return md5_hash.hexdigest()

def make_id_for_user(username,password:str):
    res = ""
    for i in str(username)+str(password) :
         res += make_hash_from_str(i)

    return res
    

# print(make_hash_from_str("true")) # b326b5062b2f0e69046810717534cb09
# print(make_hash_from_str("false"))# 68934a3e9455fa72420237eb05902327

#print(make_id_for_user("parsiya","1234"))

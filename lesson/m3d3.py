import requests
#
# r = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
#
# print(r.status_code)
# p = r.json()[:3]
#
# for i in p:
#     print(f"{i["Rate"]} - {i["Ccy"]}")

# import pprint
#
# pprint.pp({"user":{"id":101,"name":"Alice Smith","email":"alice@example.com","roles":["admin","editor"],"status":{"active":True,"last_login":"2026-10-06"}}})
#
# import json
#
# data = {"user":{"id":101,"name":"Alice Smith","email":"alice@example.com","roles":["admin","editor"],"status":{"active":True,"last_login":"2026-10-06"}}}
# print(json.dumps(data, indent=4))

yangi_user = {"ism": "Ali", "yosh": 15, "kurs": "Python"}
r = requests.post("https://httpbin.org/post", json=yangi_user)

print(r.status_code)
print(r.json()["json"])